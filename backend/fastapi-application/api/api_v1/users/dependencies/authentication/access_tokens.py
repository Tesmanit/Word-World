from typing import TYPE_CHECKING

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper
from core.models import AccessToken
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase

    

async def get_access_token_db(
    session: AsyncSession = Depends(db_helper.session_getter),
):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)