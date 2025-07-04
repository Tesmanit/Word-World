from typing import TYPE_CHECKING

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper
from core.models.user import User
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

async def get_user_db(session: AsyncSession = Depends(db_helper.session_getter)):
    yield SQLAlchemyUserDatabase(session, User)

# async def get_user_db(session: AsyncSession = Depends(db_helper.session_getter)):
#     yield User.get_db(session=session)
