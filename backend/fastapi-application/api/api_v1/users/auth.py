from fastapi import APIRouter

from core.config import settings
from .fastapi_users_router import fastapi_users
from .dependencies.authentication.backend import authentication_backend
from core.schemas.user import UserRead, UserCreate, UserUpdate

router = APIRouter(prefix=settings.api.v1.auth, tags = ['Auth'])

router.include_router(router=fastapi_users.get_auth_router(authentication_backend))
router.include_router(router=fastapi_users.get_register_router(UserRead, UserCreate))