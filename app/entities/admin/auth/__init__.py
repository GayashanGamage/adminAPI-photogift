from .login import router as login_router
from .send_email import router as send_emails
from fastapi import APIRouter

router = APIRouter(prefix="/admin/auth", tags=["admin-auth"])
router.include_router(login_router )
router.include_router(send_emails )