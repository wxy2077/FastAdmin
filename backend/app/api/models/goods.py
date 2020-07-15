#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 15:54
# @Author  : CoderCharm
# @File    : goods.py
# @Software: PyCharm
# @Desc    :
"""
商品models

参考
https://raw.githubusercontent.com/iamdarcy/hioshop-server/master/hiolabsDB.sql

"""

from sqlalchemy import Column, Integer, VARCHAR, SmallInteger, DECIMAL, TEXT
from api.db.base_class import Base, gen_uuid


class MallGoods(Base):
    """
    商品表详情
    """
    __tablename__ = "mall_goods"
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
    __table_args__ = ({'comment': '商品详情'})


class MallCategory(Base):
    """
    商品分类
    """
    name = Column(VARCHAR(64), comment="分类名称")
    front_desc = Column(VARCHAR(256), comment="分类描述")
    parent_id = Column(Integer, index=True, comment="父id")
    sort_order = Column(SmallInteger, default=10, comment="排序")
    icon_url = Column(VARCHAR(256), comment="分类显示icon")
    enabled = Column(SmallInteger, default=1, comment="是否开启 0=为开启 1=开启", server_default="1")


class MallGoodsSpecification(Base):
    """
    商品规格sku
    """
    good_id = Column(VARCHAR(128), comment="对应商品id")
    name = Column(VARCHAR(64), comment="商品规格名称 如重量 长度 颜色")
    unit = Column(VARCHAR(16), comment="规格单位 如斤 克")
    memo = Column(VARCHAR(64), comment="补充说明 如每袋5个装")
    stock = Column(Integer, comment="库存")

    __table_args__ = ({'comment': '商品规格'})


class MallGoodsGallery(Base):
    """
    商品展示
    """
    goods_id = Column(SmallInteger, default=0, index=True, comment="商品id")
    image_url = Column(VARCHAR(256), default=None)
    image_desc = Column(VARCHAR(64), default=None, nullable=True, comment="描述")
    sort_order = Column(SmallInteger, default=10, comment="排序")
    enabled = Column(SmallInteger, default=1, comment="是否开启 0=为开启 1=开启", server_default="1")
    __table_args__ = ({'comment': '商品列表'})


class MallGoodsKeywords(Base):
    """
    商品关键词
    """
    keyword = Column(VARCHAR(128), comment="关键词")
    is_hot = Column(SmallInteger, default=0, index=True, comment="是否热点")
    is_default = Column(SmallInteger, default=0, comment="是否热点")
    is_show = Column(SmallInteger, default=1, comment="是否展示")
    sort_order = Column(Integer, default=100, comment="排序")
    scheme_url = Column(VARCHAR(128), nullable=True, comment="关键词跳转链接")
    __table_args__ = ({'comment': '商品关键词'})


class MallBanner(Base):
    """
    轮播图
    """
    prc = Column(VARCHAR(256), comment="图片url")
    link = Column(VARCHAR(256), nullable=True, comment="跳转地址(或者关联商品)")
    goods_id = Column(VARCHAR(128), nullable=True, comment="关联商品")
    sort_order = Column(Integer, default=100, comment="排序")
    enabled = Column(SmallInteger, default=1, comment="是否开启 0=为开启 1=开启", server_default="1")
    banner_position = Column(VARCHAR(64), default="home", comment="轮播图位置 默认首页 首页home 个人中心profile ")
