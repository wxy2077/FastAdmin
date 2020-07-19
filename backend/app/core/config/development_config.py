#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 14:47
# @Author  : CoderCharm
# @File    : development_config.py
# @Software: PyCharm
# @Desc    :
"""
开发环境配置


"""

import os
from typing import List, Union, Any

from pydantic import AnyHttpUrl, BaseSettings, validator, IPvAnyAddress, EmailStr


class Settings(BaseSettings):

    DEBUG: bool = True
    #
    API_V1_STR: str = "/api/mall/v1"
    # SECRET_KEY: str = secrets.token_urlsafe(32)
    # SECRET_KEY 记得保密生产环境 不要直接写在代码里面
    SECRET_KEY: str = "(-ASp+_)-Ulhw0848hnvVG-iqKyJSD&*&^-H3C9mqEqSl8KN-YRzRE"

    # token过期时间 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # 根路径
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # 项目信息
    PROJECT_NAME: str = "FastAdmin"
    DESCRIPTION: str = "更多信息查看 https://www.charmcode.cn/"
    SERVER_NAME: str = "API_V1"
    SERVER_HOST: AnyHttpUrl = "http://127.0.0.1:8020"
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    # 跨域
    BACKEND_CORS_ORIGINS: List[str] = ['*']

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # mysql 配置
    MYSQL_USERNAME: str = 'root'
    MYSQL_PASSWORD: str = "Admin12345-"
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "172.16.137.129"
    MYSQL_DATABASE: str = 'FastAdmin'

    # mysql地址
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@" \
                              f"{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"

    # 基本角色权限 个人没做过权限设置 但是也看过一些开源项目就这样设计吧
    DEFAULT_ROLE: List[dict] = [
        {"role_id": 100, "role_name": "普通员工", "permission_id": 100},
        {"role_id": 500, "role_name": "主管", "permission_id": 500},
        {"role_id": 999, "role_name": "超级管理员", "permission_id": 999, "re_mark": "最高权限的超级管理员"},
    ]

    # 默认生成用户数据
    FIRST_SUPERUSER: str = "王小右"
    FIRST_MALL: EmailStr = "wg_python@163.com"
    FIRST_SUPERUSER_PASSWORD: str = "admin12345"
    FIRST_ROLE: int = 999  # 超级管理员
    FIRST_AVATAR: AnyHttpUrl = "https://avatar-static.segmentfault.com/106/603/1066030767-5d396cc440024_huge256"

    class Config:
        case_sensitive = True


settings = Settings()
