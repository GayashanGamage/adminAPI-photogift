from app.infra.registry import service_container
from fastapi import Request
from fastapi import HTTPException
from datetime import datetime

def rate_limit(accepted_request_count=2, spill_time=10):
    def rate_limit_inner(request:Request):
        # create bucket key
        bucket_key = open_rate_limit_key(request=request)
        
        # curent time
        current_time = int(datetime.now().timestamp())

        # leaked rate
        leaked_rate = accepted_request_count / spill_time

        bucket_level = service_container.cache().hget(bucket_key, 'level')
        bucket_last_update = service_container.cache().hget(bucket_key, 'last_update')

        if bucket_level is None or bucket_last_update is None:
            service_container.cache().hset(bucket_key, 'level', 1)
            service_container.cache().hset(bucket_key, 'last_update', current_time)
            service_container.cache().expire(bucket_key, spill_time)
        else:
            elaped_time = current_time - int(bucket_last_update)
            leaked = elaped_time * leaked_rate

            bucket_level = max(0, float(bucket_level) - leaked)

            if bucket_level + 1 > accepted_request_count:
                service_container.cache().hset(bucket_key, "level", bucket_level )
                service_container.cache().hset(bucket_key, "last_update", current_time)
                service_container.cache().expire(bucket_key, spill_time * 2)
                raise HTTPException(status_code=429, detail="Too Many Requests")
            else:
                bucket_level += 1
                service_container.cache().hset(bucket_key, "level", bucket_level )
                service_container.cache().hset(bucket_key, "last_update", current_time)
                service_container.cache().expire(bucket_key, spill_time * 2)

    return rate_limit_inner

def open_rate_limit_key(request):
    """
    purpose : create a key for the redis-db 
    request : 'Request' data got from endpoint
    """
    return f'{request.client.host}-{request.url.path}-{request.method}'
