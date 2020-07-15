from typing import Generator, Optional

from fastapi import Depends, Header
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

# from api import models, crud, schemas
from core import security
from core.config import settings
from api.db.session import SessionLocal
from api.models import auth
from api.admin.auth import schemas
from api.admin.auth import crud

from api.utils import custom_exc
from api.extensions import logger

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login/access-token"
)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), token: Optional[str] = Header(None)
) -> auth.AdminUser:
    """
    根据header中token 获取当前用户
    :param db:
    :param token:
    :return:
    """
    if not token:
        raise custom_exc.UserTokenError(err_desc='headers not found token')
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise custom_exc.UserTokenError(err_desc="access token fail")
    user = crud.curd_user.get(db, id=token_data.sub)
    if not user:
        raise custom_exc.UserNotFound(err_desc="user not found")
    return user


# def get_current_active_user(
#     current_user: models.User = Depends(get_current_user),
# ) -> models.User:
#     if not crud.user.is_active(current_user):
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user
#
#
# def get_current_active_superuser(
#     current_user: models.User = Depends(get_current_user),
# ) -> models.User:
#     if not crud.user.is_superuser(current_user):
#         raise HTTPException(
#             status_code=400, detail="The user doesn't have enough privileges"
#         )
#     return current_user
