from fastapi import FastAPI, Depends
from app.core.ratelimites.leaky_bucket import rate_limit
from typing import Annotated
# from app.infra.registry import service_container

app = FastAPI()

@app.get('/')
def helth_check( _: Annotated[None, Depends(rate_limit(accepted_request_count=2, spill_time=10))]):
    return {"message": "Hello World!"}


# @app.post('/post')
# def cache_test():
#     service_container.cache().hset('test', 1, 'value1')
#     output = service_container.cache().hgetall('test')

#     for key, value in output.items():
#         key = int(key)
#         value = int(value)

#     print(key, value)
#     return {"message": "Hello World!"}