#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 14:16
# @Author  : CoderCharm
# @File    : auth.py
# @Software: PyCharm
# @Desc    :
"""

用户模块

"""
import uuid

from sqlalchemy import Boolean, Column, Integer, String, VARCHAR, BIGINT
from app.api.db.base_class import Base


def gen_id():
    return uuid.uuid4().hex


class AdminUser(Base):
    """
    管理员用户表
    """
    __tablename__ = "admin_user"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(32), default=gen_id, comment="用户id")
    email = Column(String(128), unique=True, index=True, nullable=False, comment="邮箱")
    phone = Column(VARCHAR(16), unique=True, index=True, nullable=True, comment="手机号")
    nickname = Column(String(128), comment="用户昵称")
    avatar = Column(String(256), comment="用户头像")
    hashed_password = Column(String(128), nullable=False, comment="密码")
    is_active = Column(Boolean(), default=False, comment="邮箱是否激活")
    role_id = Column(Integer, comment="角色表")


class AdminRole(Base):
    """
    简单的用户角色表设计
    """
    role_id = Column(Integer, primary_key=True, index=True, comment="角色Id")
    role_name = Column(String(64), comment="角色名字")
    permission_id = Column(BIGINT, comment="权限ID")
    re_mark = Column(String(128), comment="备注信息")

