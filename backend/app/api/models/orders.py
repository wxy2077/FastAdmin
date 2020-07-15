#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 14:38
# @Author  : CoderCharm
# @File    : orders.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""
from datetime import datetime

from sqlalchemy import Column, Integer, VARCHAR, SmallInteger, DateTime, DECIMAL
from api.db.base_class import Base, gen_uuid


class MallOrder(Base):
    """
    订单表
    """
    order_id = Column(VARCHAR(20), default=gen_uuid, index=True, unique=True, comment="订单id")
    user_id = Column(Integer, index=True, comment="用户Id")
    phone = Column(VARCHAR(64), comment="手机号")
    order_status = Column(SmallInteger, index=True, comment="订单状态 101：未付款、102：已取消、103已取消(系统)、201：已付款、"
                                                "202：订单取消，退款中、203：已退款、301：已发货、302：已收货、303：已收货(系统)、"
                                                "401：已完成、801：拼团中,未付款、802：拼团中,已付款")
    offline_pay = Column(Integer, default=0, comment="线下支付订单标志")
    shipping_status = Column(Integer, default=0, comment="发货状态")
    consignee = Column(VARCHAR(64), default=0, comment="支付状态")
    country_id = Column(Integer, default=0, comment="国家")
    province_id = Column(Integer, default=0, comment="省")
    city_id = Column(Integer, default=0, comment="市")
    district_id = Column(Integer, default=0, comment="区")
    address = Column(VARCHAR(128), comment="详细地址")
    postscript = Column(VARCHAR(128), nullable=True, comment="用户留言备注")
    admin_memo = Column(VARCHAR(128), nullable=True, comment="管理员留言备注")
    print_status = Column(Integer, default=0, comment="打印状态")
    print_info = Column(VARCHAR(128), comment="打印信息")
    shipping_fee = Column(DECIMAL(10, 2), comment="免邮的商品的邮费，这个在退款时不能退给客户")
    pay_name = Column(VARCHAR(128), comment="支付名称")
    pay_id = Column(VARCHAR(255), default=0, comment="支付ID")
    pay_status = Column(Integer, index=True, default=0, comment="支付状态")
    change_price = Column(DECIMAL(10, 2), default=0.0, comment="0没改价，不等于0改过价格，这里记录原始的价格")
    actual_price = Column(DECIMAL(10, 2), default=0.0, comment="实际需要支付的金额")
    order_price = Column(DECIMAL(10, 2), default=0.0, comment="订单总价")
    goods_price = Column(DECIMAL(10, 2), default=0.0, comment="商品总价")
    add_time = Column(DateTime, default=datetime.now, comment="添加时间")
    pay_time = Column(DateTime, nullable=True, comment="支付时间")
    shipping_time = Column(DateTime, nullable=True, comment="发货时间")
    confirm_time = Column(DateTime, nullable=True, comment="确认时间")
    dealdone_time = Column(DateTime, nullable=True, comment="成交时间，用户评论或自动好评时间")
    freight_price = Column(Integer, nullable=True, comment="配送费用")
    express_value = Column(DECIMAL(10, 2), nullable=True, comment="顺丰保价金额")
    remark = Column(VARCHAR(256), default="需电联客户请优先派送勿放快递柜")
    order_type = Column(SmallInteger, default=0, comment="订单类型：0普通，1秒杀，2团购，3返现订单,7充值，8会员")
    __table_args__ = ({'comment': '订单表'})


class MallOrderExpress(Base):
    """
    快递订单表
    """
    order_id = Column(VARCHAR(20), index=True, comment="订单id")
    shipper_id = Column(VARCHAR(20), comment="物流公司Id")
    shipper_name = Column(VARCHAR(20), comment="物流公司名称")
    shipper_code = Column(VARCHAR(20), comment="物流公司代码")
    logistic_code = Column(VARCHAR(20), comment="快递单号")
    traces = Column(VARCHAR(20), comment="物流跟踪信息")
    is_finish = Column(SmallInteger, default=0, comment="是否完成 0否 1是")
    request_count = Column(Integer, default=0, comment="总查询次数")
    request_time = Column(DateTime, nullable=True, comment="最近一次查询时间")
    express_type = Column(Integer, default=0, comment="快递类型")
    region_code = Column(Integer, default=0, comment="快递的地区编码，如杭州571")
    __table_args__ = ({'comment': '订单物流表'})


class MallOrderGoods(Base):
    """
    订单商品
    """
    order_id = Column(VARCHAR(20), index=True, comment="订单id")
    user_id = Column(VARCHAR(32), comment="用户id")
    goods_id = Column(VARCHAR(20), index=True, comment="商品id")
    goods_name = Column(VARCHAR(20), comment="商品名称")
    goods_aka = Column(VARCHAR(20), nullable=True, comment="商品别称")
    number = Column(SmallInteger, default=1, comment="数量")
    retail_price = Column(DECIMAL(10, 2), default=0.00, comment="零售价")
    goods_specifition_name_value = Column(VARCHAR(256), comment="规格")
    goods_specifition_ids = Column(VARCHAR(256), comment="商品规格id")
    list_pic_url = Column(VARCHAR(256), comment="商品图片")
    __table_args__ = ({'comment': '订单商品表'})


class MallCart(Base):
    """
    购物车
    """
    user_id = Column(VARCHAR(32), index=True, comment="用户id")
    goods_id = Column(VARCHAR(20), index=True, comment="商品id")
    goods_num = Column(Integer, comment="数量")
    retail_price = Column(DECIMAL(10, 2), comment="零售价,单价")

    __table_args__ = ({'comment': '购物车'})

