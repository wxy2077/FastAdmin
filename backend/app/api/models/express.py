#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 15:08
# @Author  : CoderCharm
# @File    : express.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
物流模块
"""

from sqlalchemy import Column, Integer, VARCHAR, SmallInteger, DECIMAL
from api.db.base_class import Base


class MallShipper(Base):
    """
    快递信息
    """
    shipper_name = Column(VARCHAR(128), comment="物流公司名称")
    shipper_code = Column(VARCHAR(128), comment="物流公司代码")
    sort_order = Column(Integer, default=10, comment="排序")
    month_code = Column(VARCHAR(16), comment="月份")
    customer_name = Column(VARCHAR(16), comment="用户名")
    enabled = Column(SmallInteger, default=1, comment="是否开启 0=为开启 1=开启", server_default="1")
    __table_args__ = ({'comment': '快递信息'})


class MallRegion(Base):
    """
    地区表
    """
    parent_id = Column(SmallInteger, default=0, index=True, comment="父id")
    region_name = Column(VARCHAR(128), default="", comment="地区名称")
    region_type = Column(SmallInteger, default=2, comment="地区类型")
    agency_id = Column(SmallInteger, default=0, index=True)
    area = Column(VARCHAR(64), default="", comment="方位，根据这个定运费")
    area_code = Column(VARCHAR(8), default="0", comment="方位代码")
    far_area = Column(SmallInteger, default=0, comment="偏远地区")
    __table_args__ = ({'comment': '地区'})


class MallExceptArea(Base):
    """
    偏远地区表
    """
    content = Column(VARCHAR(256), comment="地区名称")
    area = Column(VARCHAR(256), comment="地区地区id ,隔开如 6,30,31,32")


class MallFreightTemplate(Base):
    """
    运费模版
    """
    name = Column(VARCHAR(128), nullable=True, comment="运费模版名称")
    package_price = Column(DECIMAL(10, 2), default=0.00, comment="包装费用")
    freight_type = Column(SmallInteger, default=0, comment="0=按件 1=按重量")

    __table_args__ = ({'comment': '运费模版'})
