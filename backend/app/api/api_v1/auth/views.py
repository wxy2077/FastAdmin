#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 14:11
# @Author  : CoderCharm
# @File    : views.py
# @Software: PyCharm
# @Desc    :
"""

"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def hello():
    return {"hello": "test"}
