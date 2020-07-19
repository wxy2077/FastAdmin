#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 11:00
# @Author  : CoderCharm
# @File    : role.py
# @Software: PyCharm
# @Desc    :
"""
角色表crud操作
"""

from typing import Optional
from sqlalchemy.orm import Session

from api.common.curd_base import CRUDBase
from api.models.auth import AdminRole
from api.api_v1.auth.schemas import RoleCreate, RoleUpdate


class CRUDRole(CRUDBase[AdminRole, RoleCreate, RoleUpdate]):

    @staticmethod
    def query_role(db: Session, *, role_id: int) -> Optional[AdminRole]:
        """
        此role_id是否存在
        :param db:
        :param role_id:
        :return:
        """
        return db.query(AdminRole).filter(AdminRole.role_id == role_id).first()

    def create(self, db: Session, *, obj_in: RoleCreate) -> AdminRole:
        db_obj = AdminRole(
            role_id=obj_in.role_id,
            role_name=obj_in.role_name,
            permission_id=obj_in.permission_id,
            re_mark=obj_in.re_mark
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


curd_role = CRUDRole(AdminRole)
