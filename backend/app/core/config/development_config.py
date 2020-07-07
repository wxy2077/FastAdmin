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

import secrets
from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, validator, IPvAnyAddress, EmailStr


class Settings(BaseSettings):
    #
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    PROJECT_NAME: str = "FastAdmin"
    SERVER_NAME: str = "API_V1"
    SERVER_HOST: AnyHttpUrl = "http://127.0.0.1:8020"
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    # 跨域
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ['http://localhost']

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

    FIRST_SUPERUSER: str = "admin"
    FIRST_MALL: EmailStr = "wg_python@163.com"
    FIRST_SUPERUSER_PASSWORD: str = "admin12345"
    FIRST_ROLE: int = 100

    class Config:
        case_sensitive = True


settings = Settings()
