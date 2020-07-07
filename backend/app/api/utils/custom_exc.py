#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 11:13
# @Author  : CoderCharm
# @File    : custom_exc.py
# @Software: PyCharm
# @Desc    :
"""

自定义异常

"""


class PostParamsError(Exception):
    def __init__(self, err_desc: str="POST请求参数错误"):
        self.err_desc = err_desc

