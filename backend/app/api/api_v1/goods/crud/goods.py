#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 10:21
# @Author  : CoderCharm
# @File    : goods.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

"""

from pydantic import conint
from sqlalchemy import func
from sqlalchemy.orm import Session
# from sqlalchemy.ext.serializer import dumps

from api.common.curd_base import CRUDBase
from api.models.goods import MallCategory
from ..schemas.goods import CategoryCreate, CategoryUpdate


class CRUDCategory(CRUDBase[MallCategory, CategoryCreate, CategoryUpdate]):

    def query_obj(self, db: Session, *, cate_id: int) -> dict:
        """
        查询单条数据
        :param db:
        :param cate_id:
        :return:
        """
        obj = self.get(db=db, id=cate_id)
        if not obj:
            return {}
        return {"id": obj.id, 'create_time': obj.create_time.strftime('%Y-%m-%d %H:%M:%S'), "name": obj.name,
                "front_desc": obj.front_desc, "parent_id": obj.parent_id, "sort_order": obj.sort_order,
                "icon_url": obj.icon_url, "enabled": obj.enabled}

    @staticmethod
    def query_all(db: Session, *, page: int = 1, page_size: conint(le=50) = 10) -> dict:
        """
        查询数据列表
        :param db:
        :param page:
        :param page_size:
        :return:
        """
        temp_page = (page - 1) * page_size
        # 查询数量
        total = db.query(func.count(MallCategory.id)).filter(MallCategory.is_delete == 0,
                                                             MallCategory.parent_id.is_(None)).scalar()
        # 查询结果集
        query_obj = db.query(MallCategory).filter(MallCategory.is_delete == 0, MallCategory.parent_id.is_(None)).offset(
            temp_page).limit(page_size).all()

        items = [{"id": obj.id, 'create_time': obj.create_time.strftime('%Y-%m-%d %H:%M:%S'), "name": obj.name,
                  "front_desc": obj.front_desc, "sort_order": obj.sort_order,
                  "icon_url": obj.icon_url, "enabled": obj.enabled} for obj in query_obj]
        return {
            "items": items,
            "total": total
        }

    def create(self, db: Session, *, obj_in: CategoryCreate) -> MallCategory:
        db_obj = MallCategory(
            name=obj_in.name,
            front_desc=obj_in.front_desc,
            sort_order=obj_in.sort_order,
            icon_url=obj_in.icon_url,
            enabled=obj_in.enabled
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def update_cate(db: Session, *, obj_in: CategoryUpdate):
        db.query(MallCategory).filter(MallCategory.id == obj_in.id).update({
            MallCategory.name: obj_in.name,
            MallCategory.front_desc: obj_in.front_desc,
            MallCategory.sort_order: obj_in.sort_order,
            MallCategory.icon_url: obj_in.icon_url,
            MallCategory.enabled: obj_in.enabled
        })
        db.commit()


curd_category = CRUDCategory(MallCategory)
