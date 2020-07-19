#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 13:37
# @Author  : CoderCharm
# @File    : views.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.common import deps
from api.utils import response_code
from api.extensions import logger
from api.models import auth
from .schemas.goods import CategoryCreate
from .crud.goods import curd_category
from core.config import settings

router = APIRouter()


@router.post("/add/goods", summary="添加商品")
async def goods_add(current_user: auth.AdminUser = Depends(deps.get_current_user)):
    """
    用户退出
    :param current_user:
    :return:
    """
    logger.info(settings.BASE_DIR)
    return response_code.resp_200(data="ok")


@router.post("/add/category", summary="添加分类")
async def goods_add(goods_category: CategoryCreate, db: Session = Depends(deps.get_db),current_user: auth.AdminUser = Depends(deps.get_current_user)):
    """
    用户退出
    :param goods_category:
    :param current_user:
    :return:
    """
    curd_category.create(db=db, obj_in=goods_category)
    return response_code.resp_200(data="ok")
