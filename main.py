from fastapi import FastAPI, Depends
from app.core.ratelimites.leaky_bucket import rate_limit
from typing import Annotated
from app.core.response import response
from app.core.response_code import response_codes
from app.core.errors.error_handler import error_response
from app.core.errors.app_errors import AppError

app = FastAPI()

app.add_exception_handler(AppError, error_response)

@app.get('/')
def helth_check( num : int, _: Annotated[None, Depends(rate_limit(accepted_request_count=2, spill_time=10))]):
    if num == 1:
        raise AppError(
            message='User not found',
            status_code=404,
            code=response_codes.user_not_found
        )
    return response(
        message='Hello, World!',
        code=response_codes.user_created,
        status_code=200)