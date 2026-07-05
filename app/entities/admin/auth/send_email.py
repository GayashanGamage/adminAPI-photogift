from brevo import Brevo
from brevo.transactional_emails import SendTransacEmailRequestSender, SendTransacEmailRequestToItem
from app.infra.registry import service_initiate
from typing import Optional
from pydantic import BaseModel, EmailStr
from app.core.email_template import EmailTemplate
from app.core.response import response
from app.core.response_code import response_codes
from fastapi import APIRouter
from app.core.roles import Role

servicess = service_initiate()


class EmailInfo(BaseModel):
    user_id : str
    to: str
    template_id: int
    senderName : str
    senderEmail : EmailStr
    toName : str
    toEmail : EmailStr
    other_data : EmailData
    role : Role

class EmailData(BaseModel):
    tem_password : str

router = APIRouter()

@router.post("/send-email")
async def send_email(data : EmailInfo):
    # evaluate the where requrest came from
    # send email using brevo
    try:
        servicess.email().transactional_emails.send_transac_email(
            params={
                "role" : f'{data.role.value}',
                "temp_password" : f'{data.other_data.tem_password}'
            },
            sender=SendTransacEmailRequestSender(
                name=data.senderName,
                email=data.senderEmail
            ),
            to=[SendTransacEmailRequestToItem(
                email=data.toEmail,
                name=data.toName
            )],
            template_id=int(EmailTemplate.ACCOUNT_CREATION.value)
        )
    except Exception as e:
        return {"error": str(e)}
    
    # store in database
    
    # return output
    return response(
        status_code= 200,
        message= 'email sent successfully',
        code= response_codes.email_sent
    )