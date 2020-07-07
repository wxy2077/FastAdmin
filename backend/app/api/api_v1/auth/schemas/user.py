#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 16:23
# @Author  : CoderCharm
# @File    : user.py
# @Software: PyCharm
# @Desc    :
"""

user_id = Column(String(32), default=gen_id, comment="用户id")
email = Column(String(128), unique=True, index=True, nullable=False, comment="邮箱")
phone = Column(VARCHAR(16), unique=True, index=True, nullable=False, comment="手机号")
nickname = Column(String(128), comment="用户昵称")
hashed_password = Column(String(128), nullable=False, comment="密码")
is_active = Column(Boolean(), default=False, comment="是否激活")
role_id = Column(Integer, comment="角色表")

"""

from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    phone: int = None
    is_active: Optional[bool] = True


# Properties to receive via API on creation
class UserCreate(UserBase):
    nickname: str
    email: EmailStr
    password: str
    role_id: int


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class UserInDB(UserInDBBase):
    hashed_password: str

