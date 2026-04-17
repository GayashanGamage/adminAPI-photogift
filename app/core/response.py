from fastapi.responses import JSONResponse
from app.core.response_code import response_codes


def response(message: str, code: response_codes, status_code: int, data : dict | list | None = None):
    return JSONResponse(
        content={
            "message": message,
            "code": code.value,
            "status_code": status_code,
            "data": data
        },
        status_code=status_code
    )