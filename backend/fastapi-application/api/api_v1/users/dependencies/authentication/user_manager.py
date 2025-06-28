from typing import TYPE_CHECKING, Annotated
from fastapi import Depends

from .users import get_user_db
from core.authentication.user_manager import UserManager

if TYPE_CHECKING:
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)