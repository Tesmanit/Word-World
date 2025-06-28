import uuid

from fastapi_users import FastAPIUsers

from core.models import User
from .dependencies.authentication.user_manager import get_user_manager
from .dependencies.authentication.backend import authentication_backend
from core.models.user import UserIdType

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)