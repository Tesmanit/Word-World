from fastapi import APIRouter

from core.config import settings
from .fastapi_users_router import fastapi_users
from .dependencies.authentication.backend import authentication_backend
from core.schemas.user import UserRead, UserCreate, UserUpdate

router = APIRouter(prefix=settings.api.v1.users, tags = ['Users']) 
router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate))