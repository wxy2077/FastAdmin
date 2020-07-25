#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 17:01
# @Author  : CoderCharm
# @File    : token_schema.py
# @Software: PyCharm
# @Desc    :
"""

"""

from typing import Optional
from pydantic import BaseModel

from api.common.schemas_base import RespBase


class Token(BaseModel):
    token: str


class TokenPayload(BaseModel):
    sub: Optional[int] = None


class RespToken(RespBase):
    # 认证响应模型
    data: Token
