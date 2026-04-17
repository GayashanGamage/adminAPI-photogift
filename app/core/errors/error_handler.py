from fastapi.responses import JSONResponse
from fastapi import Request
from app.core.errors.app_errors import AppError

def error_response(req : Request, exe : AppError):
    return JSONResponse(
        content={
            "message": exe.message,
            "code": exe.code,
            "status_code" : exe.status_code,
            "data" : exe.data
        },
        status_code=exe.status_code
    )