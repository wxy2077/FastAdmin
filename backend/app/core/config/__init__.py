#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 15:34
# @Author  : CoderCharm
# @File    : __init__.py.py
# @Software: PyCharm
# @Desc    :
"""
配置文件

更具环境变量 区分生产开发

"""

import os

# 获取环境变量
env = os.getenv("ENV", "")
if env:
    # 如果有虚拟环境 则是 生产环境
    print("----------生产环境启动------------")
    from .production_config import settings
else:
    # 没有则是开发环境
    print("----------开发环境启动------------")
    from .development_config import settings

