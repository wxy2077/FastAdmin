#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 16:38
# @Author  : CoderCharm
# @File    : curd_user.py
# @Software: PyCharm
# @Desc    :
"""

"""

from typing import Optional

from sqlalchemy.orm import Session

from core.security import get_password_hash, verify_password
from api.common.curd_base import CRUDBase
from api.models.auth import AdminUser
from api.admin.auth.schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[AdminUser, UserCreate, UserUpdate]):

    @staticmethod
    def get_by_email(db: Session, *, email: str) -> Optional[AdminUser]:
        """
        通过email获取用户
        参数里面的* 表示 后面调用的时候 要用指定参数的方法调用
        正确调用方式
            curd_user.get_by_email(db, email="xxx")
        错误调用方式
            curd_user.get_by_email(db, "xxx")
        :param db:
        :param email:
        :return:
        """
        return db.query(AdminUser).filter(AdminUser.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> AdminUser:
        db_obj = AdminUser(
            nickname=obj_in.nickname,
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            avatar=obj_in.avatar,
            role_id=obj_in.role_id,
            is_active=obj_in.is_active
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    # def update(
    #         self, db: Session, *, db_obj: AdminUser, obj_in: Union[UserUpdate, Dict[str, Any]]
    # ) -> AdminUser:
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.dict(exclude_unset=True)
    #     if update_data["password"]:
    #         hashed_password = get_password_hash(update_data["password"])
    #         del update_data["password"]
    #         update_data["hashed_password"] = hashed_password
    #     return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[AdminUser]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: AdminUser) -> bool:
        return user.is_active

    def is_superuser(self, user: AdminUser) -> bool:
        return user.is_superuser


curd_user = CRUDUser(AdminUser)
