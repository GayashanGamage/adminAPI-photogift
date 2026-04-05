from app.infra.registry import service_container
from fastapi import Request
from fastapi import HTTPException
from datetime import datetime, timedelta


def rate_limit(accepted_request_count=2, time_limit=10):
    """
    purpose : apply retelimites on endpoints

    accepted_request_count : how many request can accept withing given sliding_window
    time_limit : sliding_window time fram
    """
    def rate_limit_inner(request:Request):
        # create redis key
        redis_key = open_rate_limit_key(request=request)

        # get the existing data from redis
        request_list = service_container.cache().zrange(key=redis_key, start=0, stop=accepted_request_count, withscores=True)

        # if length is more than 0
        if len(request_list) > 0:
            # get oldest item
            last_item = datetime.fromtimestamp(request_list[0][1])

            # remove lastone is time is exceedrate_limit
            if (datetime.now() - last_item) > timedelta(seconds=time_limit):
                service_container.cache().zpopmin(key=redis_key)

                # directly add the new request
                service_container.cache().expire(redis_key, time_limit)
            
            # check the current request count
            # else: 
            elif len(request_list) < accepted_request_count:
                # if less than, add new request
                service_container.cache().zadd(redis_key, { str(len(request_list)) : int(datetime.now().timestamp())})
                service_container.cache().expire(redis_key, time_limit)

            # else show ratelimit error
            else:
                raise HTTPException(
                            status_code=419, 
                            detail="exceed the rate limit"
                        )
            
        # else lenght is equal to zero
        else:
            service_container.cache().zadd(redis_key, {len(request_list): int(datetime.now().timestamp())})
            service_container.cache().expire(redis_key, time_limit)
        

    return rate_limit_inner


def open_rate_limit_key(request):
    """
    purpose : create a key for the redis-db 
    request : 'Request' data got from endpoint
    """
    return f'{request.client.host}-{request.url.path}-{request.method}'