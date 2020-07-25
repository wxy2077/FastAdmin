#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 16:23
# @Author  : CoderCharm
# @File    : user_schema.py
# @Software: PyCharm
# @Desc    :
"""

"""

from typing import Optional, Union

from pydantic import BaseModel, EmailStr, AnyHttpUrl


from api.common.schemas_base import RespBase


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    phone: int = None
    is_active: Optional[bool] = True


class UserAuth(BaseModel):
    password: str


# 邮箱登录认证 验证数据字段都叫username
class UserEmailAuth(UserAuth):
    username: EmailStr


# 手机号登录认证 验证数据字段都叫username
class UserPhoneAuth(UserAuth):
    username: int


# 创建账号需要验证的条件
class UserCreate(UserBase):
    nickname: str
    email: EmailStr
    password: str
    role_id: int
    avatar: AnyHttpUrl


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class UserInDB(UserInDBBase):
    hashed_password: str


# 返回的用户信息
class UserInfo(BaseModel):
    role_id: int
    role: str
    nickname: str
    avatar: AnyHttpUrl


class RespUserInfo(RespBase):
    # 响应用户信息
    data: UserInfo
