#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 14:16
# @Author  : CoderCharm
# @File    : auth.py
# @Software: PyCharm
# @Desc    :
"""

用户模块

"""
from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, VARCHAR, BIGINT, SmallInteger, DateTime
from api.db.base_class import Base, gen_uuid


class AdminUser(Base):
    """
    管理员表
    """
    __tablename__ = "admin_user"
    user_id = Column(VARCHAR(32), default=gen_uuid, unique=True, comment="用户id")
    email = Column(VARCHAR(128), unique=True, index=True, nullable=False, comment="邮箱")
    phone = Column(VARCHAR(16), unique=True, index=True, nullable=True, comment="手机号")
    nickname = Column(VARCHAR(128), comment="管理员昵称")
    avatar = Column(VARCHAR(256), comment="管理员头像")
    hashed_password = Column(VARCHAR(128), nullable=False, comment="密码")
    is_active = Column(Integer, default=False, comment="邮箱是否激活 0=未激活 1=激活", server_default="0")
    role_id = Column(Integer, comment="角色表")
    __table_args__ = ({'comment': '管理员表'})


class AdminRole(Base):
    """
    简单的用户角色表设计
    """
    __tablename__ = "admin_role"
    role_id = Column(Integer, primary_key=True, index=True, comment="角色Id")
    role_name = Column(VARCHAR(64), comment="角色名字")
    permission_id = Column(BIGINT, comment="权限ID")
    re_mark = Column(VARCHAR(128), comment="备注信息")
    __table_args__ = ({'comment': '管理员角色'})


class MallUser(Base):
    """
    用户表
    """
    __tablename__ = "mall_user"
    user_id = Column(VARCHAR(32), default=gen_uuid, index=True, unique=True, comment="用户id")
    nickname = Column(VARCHAR(128), comment="用户昵称(显示用可更改)")
    username = Column(VARCHAR(128), comment="用户名(不可更改)")
    avatar = Column(VARCHAR(256), nullable=True, comment="用户头像")
    hashed_password = Column(VARCHAR(128), nullable=False, comment="密码")
    phone = Column(VARCHAR(16), unique=True, index=True, nullable=True, comment="手机号")
    gender = Column(SmallInteger, default=0, comment="性别 0=未知 1=男 2=女", server_default="0")
    register_time = Column(DateTime, default=datetime.now, comment="注册事件")
    last_login_time = Column(DateTime, default=datetime.now, comment="上次登录时间")
    last_login_ip = Column(VARCHAR(64), nullable=True, comment="上次登录IP")
    register_ip = Column(VARCHAR(64), nullable=True, comment="注册IP")
    weixin_openid = Column(VARCHAR(64), nullable=True, comment="微信openId")
    country = Column(VARCHAR(64), nullable=True, comment="国家")
    province = Column(VARCHAR(64), nullable=True, comment="省")
    city = Column(VARCHAR(64), nullable=True, comment="市")
    __table_args__ = ({'comment': '用户表'})


class MallAddress(Base):
    """
    用户地址列表
    """
    name = Column(VARCHAR(64), comment="用户昵称")
    user_id = Column(VARCHAR(32), comment="用户id")
    country_id = Column(Integer, comment="国家Id")
    province_id = Column(Integer, comment="省id")
    city_id = Column(Integer, comment="市id")
    district_id = Column(Integer, comment="区id")
    address = Column(VARCHAR(128), comment="详细地址")
    phone = Column(VARCHAR(64), comment="手机号")
    is_default = Column(SmallInteger, default=0, comment="是否默认地址", server_default="0")
    __table_args__ = ({'comment': '地址表'})


class MallSearchHistory(Base):
    """
    搜索记录
    """
    keyword = Column(VARCHAR(64), comment="搜索关键词")
    search_origin = Column(SmallInteger, default=1, comment="搜索来源 1=小程序 2=APP 3=PC", server_default="1")
    user_id = Column(VARCHAR(32), index=True, comment="用户id")
    __table_args__ = ({'comment': '搜索记录'})


class MallSiteNotice(Base):
    """
    站点消息
    """
    enabled = Column(SmallInteger, default=1, comment="是否开启 0=为开启 1=开启", server_default="1")
    content = Column(VARCHAR(256), comment="全局消息通知")
    start_time = Column(DateTime, comment="开始时间")
    end_time = Column(DateTime, comment="结束时间")

    __table_args__ = ({'comment': '站点消息'})

