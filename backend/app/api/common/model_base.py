#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 14:17
# @Author  : CoderCharm
# @File    : model_base.py
# @Software: PyCharm
# @Desc    :
"""
基础 models 类型

废弃不用

关于sqlalchemy继承
https://docs.sqlalchemy.org/en/13/orm/inheritance.html#single-table-inheritance
"""
# from datetime import datetime
#
# from sqlalchemy import Column, Integer, DateTime
# # from sqlalchemy.ext.declarative import declarative_base
#
# # Base = declarative_base()
# from app.api.db.base import Base
#
#
# class ModelBase(Base):
#     __tablename__ = 'model_base'
#     id = Column(Integer, primary_key=True, index=True)
#     create_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="创建时间")
#     update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")
#     is_delete = Column(Integer, default=0, comment="逻辑删除:0=未删除,1=删除")
#
#     __mapper_args__ = {
#         'polymorphic_on': id,
#         'polymorphic_identity': 'model_base'
#     }
