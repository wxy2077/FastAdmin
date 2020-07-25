#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 17:04
# @Author  : CoderCharm
# @File    : schemas_base.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""
from typing import Union
from pydantic import BaseModel


class RespBase(BaseModel):
    code: int
    message: str
    data: Union[dict, list, str]
