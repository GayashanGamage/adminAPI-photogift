from fastapi import FastAPI, Depends
from app.core.ratelimites.sliding_window import rate_limit
from typing import Annotated

app = FastAPI()

@app.get('/')
def helth_check( _: Annotated[None, Depends(rate_limit(accepted_request_count=2, time_limit=10))]):
    return {"message": "Hello World!"}
