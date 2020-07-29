#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 13:37
# @Author  : CoderCharm
# @File    : views.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""
from typing import Union, Any
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from api.common import deps
from api.common.logger import logger
from api.utils import response_code

from .schemas import goods_schema, category_schema
from .crud.category import curd_category

router = APIRouter()


@router.post("/add/goods", summary="添加商品")
async def goods_add(
        goods_info: goods_schema.GoodsCreate,
        db: Session = Depends(deps.get_db),
        token_data: Union[str, Any] = Depends(deps.check_jwt_token),
):
    logger.info(goods_info)
    return response_code.resp_200(data="ok")


@router.get("/query/category/list", summary="查询分类列表")
async def query_category_list(
        db: Session = Depends(deps.get_db),
        token_data: Union[str, Any] = Depends(deps.check_jwt_token),
        page: int = Query(1, ge=1, title="当前页"),
        page_size: int = Query(10, le=50, title="页码长度")
):
    logger.info(f"查询分类列表->用户id:{token_data.sub}当前页{page}长度{page_size}")
    response_result = curd_category.query_all(db, page=page, page_size=page_size)
    return response_code.resp_200(data=response_result)


@router.get("/query/category", summary="查询分类")
async def query_category(
        db: Session = Depends(deps.get_db),
        token_data: Union[str, Any] = Depends(deps.check_jwt_token),
        cate_id: int = Query(..., title="查询当前分类"),
):
    logger.info(f"查询分类->用户id:{token_data.sub}分类:{cate_id}")
    response_result = curd_category.query_obj(db, cate_id=cate_id)
    return response_code.resp_200(data=response_result)


@router.post("/add/category", summary="添加分类")
async def add_category(
        category_info: category_schema.CategoryCreate,
        db: Session = Depends(deps.get_db),
        token_data: Union[str, Any] = Depends(deps.check_jwt_token),
):
    logger.info(f"添加分类->用户id:{token_data.sub}分类名:{category_info.name}")
    curd_category.create(db=db, obj_in=category_info)
    return response_code.resp_200(message="分类添加成功")


@router.post("/modify/category", summary="修改分类")
async def modify_category(
        cate_info: category_schema.CategoryUpdate,
        db: Session = Depends(deps.get_db),
        token_data: Union[str, Any] = Depends(deps.check_jwt_token),
):
    logger.info(f"修改分类->用户id:{token_data.sub}分类id:{cate_info.id}")
    curd_category.update_cate(db=db, obj_in=cate_info)

    return response_code.resp_200(message="修改成功")


@router.post("/del/category", summary="删除分类")
async def modify_category(
        cate_ids: category_schema.CategoryDel,
        db: Session = Depends(deps.get_db),
        token_data: Union[str, Any] = Depends(deps.check_jwt_token),
):
    logger.info(f"修改分类->用户id:{token_data.sub}分类id:{cate_ids.ids}")
    for cate_id in cate_ids.ids:
        curd_category.remove(db, id=cate_id)
    return response_code.resp_200(message="删除成功")


@router.post("/enabled/category", summary="分类开启或关闭")
async def enabled_category(
        cate_info: category_schema.CategoryEnable,
        db: Session = Depends(deps.get_db),
        token_data: Union[str, Any] = Depends(deps.check_jwt_token),
):
    logger.info(f"开启分类操作->用户id:{token_data.sub}分类id:{cate_info.ids}操作:{cate_info.enabled}")
    for cate_id in cate_info.ids:
        curd_category.update_enabled(db, id=cate_id, enabled=cate_info.enabled)
    return response_code.resp_200(message="操作成功")


@router.post("/search/category", summary="搜索分类")
async def search_category(
        cate_info: category_schema.CategorySearch,
        db: Session = Depends(deps.get_db),
        token_data: Union[str, Any] = Depends(deps.check_jwt_token),
):
    logger.info(f"搜索分类操作->用户id:{token_data.sub}搜索{cate_info.key_world}:{cate_info.key_world}"
                f"页码:{cate_info.page}长度{cate_info.page_size}")
    response_result = curd_category.search_field(db, cate_info=cate_info)
    return response_code.resp_200(data=response_result)
