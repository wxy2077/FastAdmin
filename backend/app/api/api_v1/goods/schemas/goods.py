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

from pydantic import BaseModel, AnyHttpUrl


class GoodsBase(BaseModel):
    pass


class GoodsCreate(GoodsBase):
    """
    新增商品
    """

    pass


"""
name = Column(VARCHAR(64), comment="分类名称")
    front_desc = Column(VARCHAR(256), comment="分类描述")
    parent_id = Column(Integer, index=True, comment="父id")
    sort_order = Column(SmallInteger, default=10, comment="排序")
    icon_url = Column(VARCHAR(256), comment="分类显示icon")
    enabled = Column(SmallInteger, d
"""


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
   pass



