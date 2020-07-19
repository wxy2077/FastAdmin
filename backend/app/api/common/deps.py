from typing import Generator, Optional, Union, Any

from fastapi import Depends, Header
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

# from api import models, crud, schemas
from core import security
from core.config import settings
from api.db.session import SessionLocal
from api.models.auth import AdminUser
from api.api_v1.auth import schemas, crud

from api.utils import custom_exc


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def check_jwt_token(
     token: Optional[str] = Header(None)
) -> Union[str, Any]:
    """
    只解析验证token
    :param token:
    :return:
    """

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        return schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError, AttributeError):
        raise custom_exc.UserTokenError(err_desc="access token fail")


def get_current_user(
    db: Session = Depends(get_db), token: Optional[str] = Header(None)
) -> AdminUser:
    """
    根据header中token 获取当前用户
    :param db:
    :param token:
    :return:
    """
    if not token:
        raise custom_exc.UserTokenError(err_desc='headers not found token')

    token_data = check_jwt_token(token)
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
