import uuid
import logging
from typing import TYPE_CHECKING

from typing import Optional
from core import config

from fastapi_users import BaseUserManager, IntegerIDMixin
from core.models.user import UserIdType, User

log = logging.getLogger(__name__)

if TYPE_CHECKING:
    from fastapi import Request


class UserManager(IntegerIDMixin, BaseUserManager[User, UserIdType]):
    reset_password_token_secret = config.settings.access_token.reset_password_token_secret
    verification_token_secret = config.settings.access_token.verification_token_secret

    async def on_after_register(self, user: User, request: Optional["Request"] = None):
        log.warning("User %r has registered.", user.id)

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional["Request"] = None
    ):
        log.warning("User %r has forgot their password. Reset token: %r", user.id, token)

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional["Request"] = None
    ):
        log.warning("Verification requested for user %r. Verification token: %r", user.id, token)

