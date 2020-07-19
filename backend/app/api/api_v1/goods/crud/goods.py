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

from typing import Optional

from sqlalchemy.orm import Session

from api.common.curd_base import CRUDBase
from api.models.goods import MallCategory
from ..schemas.goods import CategoryCreate, CategoryUpdate


class CRUDCategory(CRUDBase[MallCategory, CategoryCreate, CategoryUpdate]):

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


curd_category = CRUDCategory(MallCategory)
