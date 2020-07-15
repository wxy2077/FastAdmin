#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 13:35
# @Author  : CoderCharm
# @File    : api.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""

from fastapi import APIRouter

from api.admin import auth

api_admin_router = APIRouter()
api_admin_router.include_router(auth.router, prefix="/admin/auth", tags=["后台管理员"])
