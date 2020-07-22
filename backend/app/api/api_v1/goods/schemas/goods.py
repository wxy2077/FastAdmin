#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 14:34
# @Author  : CoderCharm
# @File    : goods.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
验证 goods 的模型
"""
from typing import Union, List
from pydantic import BaseModel, AnyHttpUrl, conint


class GoodsBase(BaseModel):
    pass


class GoodsCreate(GoodsBase):
    """
    新增商品
    """

    pass


class CategoryCreate(BaseModel):
    """
    新增分类
    """
    name: str
    front_desc: str
    sort_order: int
    icon_url: AnyHttpUrl
    enabled: int = 1


class CategoryUpdate(CategoryCreate):
    """
    更新分类
    """
    id: Union[int, str]


class CategoryDel(BaseModel):
    """
    逻辑删除
    """
    ids: List[int]


class CategoryEnable(CategoryDel):
    """
    批量操作开启开关 继承 ids:List[int]
    """
    enabled: int


class CategorySearch(BaseModel):
    """
    搜索分类
    """
    key_world: str
    page: conint(ge=1) = 1
    page_size: conint(le=50) = 10
