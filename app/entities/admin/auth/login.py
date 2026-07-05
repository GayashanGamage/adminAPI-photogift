from fastapi import APIRouter
from app.infra.registry import service_initiate
from app.core.roles import Role
from pydantic import BaseModel, field_validator
from typing import Optional
import secrets
import string
from app.core.response import response
from app.core.response_code import response_codes
import json

# user input data validation
class User(BaseModel):
    first_name: str
    last_name: str
    role : Role
    email: str
    password: Optional[str] = None

    @field_validator("password")
    def validate_password(cls, value):
        text = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(text) for _ in range(8))
        return password

router = APIRouter()
servicess = service_initiate()

# api endpoint for create new user
@router.post("/login")
def login(user : User):
    
    # create new user in clerk
    try:
        result = servicess.auth().users.create(
            first_name = user.first_name,
            last_name = user.last_name,
            email_address = [user.email],
            password = user.password,
            public_metadata = {"role": user.role.value}
        )
    except Exception as e:
        return response(
            status_code= 500,
            message= f'{json.loads(str(e)).get("errors")[0].get("message")}',
            code= response_codes.user_not_created
        )
    
    # schedule email in qstash
    try:
        servicess.queue().message.publish_json(
            url="https://example.com",
            body={
                "hello": "world",
            },
        )
    except Exception as e:
        # try store data in db
        # try reverse the user creation in clerk
        # return error response
        return response(
            status_code= 500,
            message= f'{e}',
            code= response_codes.internal_server_error
        )
    
    # return output
    return response(
        status_code= 200,
        message= 'user created successfully',
        code= response_codes.user_created
    )