from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from typing import TYPE_CHECKING

from .mixins.int_id_pk import IntIdPkMixin
from .base import Base


UserIdType = int

class User(Base, IntIdPkMixin, SQLAlchemyBaseUserTable[UserIdType]):
    pass
    # @classmethod
    # def get_db(cls, session: AsyncSession):
    #     return SQLAlchemyUserDatabase(session, cls)