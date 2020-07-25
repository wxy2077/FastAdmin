#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 14:34
# @Author  : CoderCharm
# @File    : goods_schema.py
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
    """
    goods_id = Column(VARCHAR(128), default=gen_uuid, index=True, unique=True, comment="商品id")
    category_id = Column(Integer, default=0, index=True, comment="分类id")
    is_on_sale = Column(Integer, default=1, comment="是否售卖 0=否 1=是")
    goods_name = Column(VARCHAR(64), comment="商品名称")
    goods_number = Column(Integer, default=0, index=True, comment="商品数量")
    specification_id = Column(Integer, index=True, comment="商品规格id")
    keywords = Column(VARCHAR(256), default=0, comment="商品关键字")
    sell_volume = Column(Integer, default=0, comment="销售量")
    retail_price = Column(DECIMAL(10, 2), comment="零售价,单价")
    min_retail_price = Column(DECIMAL(10, 2), default=0, comment="最低零售价")
    cost_price = Column(DECIMAL(10, 2), default=0, comment="成本价")
    min_cost_price = Column(DECIMAL(10, 2), default=0, comment="最低成本价")
    goods_brief = Column(VARCHAR(256), comment="商品简介")
    goods_desc = Column(TEXT, comment="商品描述")
    sort_order = Column(SmallInteger, default=100, index=True, comment="排序")
    is_index = Column(SmallInteger, default=0)
    is_new = Column(SmallInteger, default=0, comment="是否新品推荐")
    goods_unit = Column(VARCHAR(45), comment="商品单位")
    list_prc_banner = Column(VARCHAR(256), comment="商品banner")
    list_pic_url = Column(VARCHAR(256), comment="商品列表图")
    freight_template_id = Column(SmallInteger, default=0, comment="配运模版id")
    freight_type = Column(VARCHAR(256), default=0, comment="配运类型")
    """
    category_id: int  # 分类
    is_on_sale: int = 1  # 是在售卖
    goods_name: str
    goods_brief: str
    list_pic_url: str
    goods_unit: str   # 商品单位
    sell_volume: int  # 销量
    goods_desc: str   # 商品详情





