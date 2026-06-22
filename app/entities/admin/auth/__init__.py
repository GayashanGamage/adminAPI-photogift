from .login import router as login_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(login_router, prefix="/admin/auth", tags=["admin-auth"])