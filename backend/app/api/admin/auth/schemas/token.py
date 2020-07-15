#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 17:01
# @Author  : CoderCharm
# @File    : token.py
# @Software: PyCharm
# @Desc    :
"""

"""

from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: Optional[int] = None
