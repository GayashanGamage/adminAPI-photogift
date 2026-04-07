from app.infra.registry import service_container
from fastapi import Request
from fastapi import HTTPException

def rate_limit(accepted_request_count=2, time_limit=10):
    
    def rate_limit_inner(request:Request):
        # create key
        redis_key = open_rate_limit_key(request=request)
        
        # get the existing key value pair
        existing_value = service_container.cache().get(redis_key)

        # check the existing key value
        if existing_value is None:
            service_container.cache().set(redis_key, 1, ex=time_limit)
            
        # if the value is less than request_count, then increase
        elif int(existing_value) < accepted_request_count:
            service_container.cache().incr(redis_key)
            
        # otherwise return 429 error
        else :
            raise HTTPException(
                    status_code=419, 
                    detail="exceed the rate limit"
                )
    
    return rate_limit_inner


def open_rate_limit_key(request):
    """
    purpose : create a key for the redis-db 
    request : 'Request' data got from endpoint
    """
    return f'{request.client.host}-{request.url.path}-{request.method}'