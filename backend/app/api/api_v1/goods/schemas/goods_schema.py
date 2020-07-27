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
    goods_name: str
    goods_brief: str  # 商品简介
    category_id: int  # 分类
    is_on_sale: int = 1  # 是在售卖
    pic_banner: str = None  # 封面 没有取轮播图第一张
    list_pic_url: str  # 轮播图
    goods_unit: str  # 商品单位
    sell_volume: int  # 销量
    goods_desc_type: int = 1  # 详情内容1=富文本 2=MarkDown
    goods_desc: str  # 商品详情
    specification_id: int  # 商品规格 重量 长度 颜色 尺码
    specification_name: str  # 商品规格名称 如
    specification_unit: str  # 规格单位 如斤 克
    specification_memo: str  # 补充说明 如每袋5个装
    goods_number: float  # 库存数量
    retail_price: float  # 零售价
    min_retail_price: float  # 最低零售价
    is_new: int = 0  # 是否新品 默认0
    freight_template_id: int  # 运费模版id
    sort_order: int = 1  # 排序
