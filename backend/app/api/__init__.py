#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 15:14
# @Author  : CoderCharm
# @File    : __init__.py.py
# @Software: PyCharm
# @Desc    :
"""

模仿Flask工厂模式

"""
import traceback

from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError, ValidationError

from app.api.api_v1.api import api_v1_router
from app.core.config import settings
from app.api.extensions import logger

from app.api.utils.custom_exc import PostParamsError, UserTokenError, UserNotFound
from app.api.utils import response_code


def create_app():
    """
    生成FatAPI对象
    :return:
    """
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.DESCRIPTION,
        docs_url=f"{settings.API_V1_STR}/docs",
        openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

    # 其余的一些全局配置可以写在这里

    # 跨域设置
    register_cors(app)

    # 注册路由
    register_router(app)

    # 注册捕获全局异常
    register_exception(app)

    return app


def register_router(app: FastAPI):
    """
    注册路由
    :param app:
    :return:
    """

    app.include_router(
        api_v1_router,
        prefix=settings.API_V1_STR     # 前缀
    )


def register_cors(app: FastAPI):
    """
    支持跨域

    貌似发现了一个bug
    https://github.com/tiangolo/fastapi/issues/133

    :param app:
    :return:
    """
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )


def register_exception(app: FastAPI):
    """
    全局异常捕获

    注意 别手误多敲一个s

    exception_handler
    exception_handlers
    两者有区别

        如果只捕获一个异常 启动会报错
        @app.exception_handlers(UserNotFound)
    TypeError: 'dict' object is not callable

    :param app:
    :return:
    """

    # 自定义异常 捕获
    @app.exception_handler(UserNotFound)
    async def user_not_found_exception_handler(request: Request, exc: UserNotFound):
        """
        用户认证未找到
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"token未知用户\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")

        return response_code.resp_5001(message=exc.err_desc)

    @app.exception_handler(UserTokenError)
    async def user_token_exception_handler(request: Request, exc: UserTokenError):
        """
        用户token异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"用户认证异常\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")

        return response_code.resp_5000(message=exc.err_desc)

    @app.exception_handler(PostParamsError)
    async def query_params_exception_handler(request: Request, exc: PostParamsError):
        """
        内部查询操作时，其他参数异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"参数查询异常\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")

        return response_code.resp_400(message=exc.err_desc)

    @app.exception_handler(ValidationError)
    async def inner_validation_exception_handler(request: Request, exc: ValidationError):
        """
        内部参数验证异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"内部参数参数错误\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return response_code.resp_500(message=exc.errors())

    @app.exception_handler(RequestValidationError)
    async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
        """
        请求参数验证异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"参数错误\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return response_code.resp_422(message=exc.errors())

    # 捕获全部异常
    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc: Exception):
        """
        全局所有异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"全局异常\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return response_code.resp_500(message="服务器内部错误")
