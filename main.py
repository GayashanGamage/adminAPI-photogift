from fastapi import FastAPI, Depends
from app.core.ratelimites.leaky_bucket import rate_limit
from typing import Annotated
from app.core.response import response
from app.core.response_code import response_codes

app = FastAPI()

@app.get('/')
def helth_check( _: Annotated[None, Depends(rate_limit(accepted_request_count=2, spill_time=10))]):
    return response(
        message='Helth Check Successfull', 
        status_code=200, 
        code=response_codes.user_created
        )
