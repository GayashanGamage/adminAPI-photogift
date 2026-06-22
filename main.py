from fastapi import FastAPI, Depends
from app.entities.admin.auth import router as auth_router

app = FastAPI()
app.include_router(auth_router)


# from app.core.ratelimites.leaky_bucket import rate_limit
# from typing import Annotated
# from app.core.response import response
# from app.core.response_code import response_codes
# from app.core.errors.error_handler import error_response
# from app.core.errors.app_errors import AppError
# from app.infra.registry import service_container
# from uuid import UUID
# from pydantic import BaseModel, EmailStr
# from clerk_backend_api import ClerkErrors


# app.add_exception_handler(AppError, error_response)

# @app.get('/')
# def helth_check( num : int, _: Annotated[None, Depends(rate_limit(accepted_request_count=2, spill_time=10))]):
#     if num == 1:
#         raise AppError(
#             message='User not found',
#             status_code=404,
#             code=response_codes.user_not_found
#         )
#     return response(
#         message='Hello, World!',
#         code=response_codes.user_created,
#         status_code=200)

# class newUser(BaseModel):
#     first_name : str | None = None
#     last_name : str | None = None
#     email : EmailStr
#     password : str


# @app.post('/newuser')
# async def create_new_user(user : newUser):
#     try:
#         new_user = service_container.auth().users.create(
#             external_id = UUID,
#             first_name = user.first_name,
#             last_name = user.last_name,
#             email_address = user.email,
#             password = user.password,
#         )
#         return response(
#             status_code= 200,
#             message= 'user created successfully',
#             code= response_codes.user_created,
#             data= new_user,
#         )
#     except ClerkErrors as e:
#         raise ClerkErrors.status_code