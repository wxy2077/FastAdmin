from fastapi import APIRouter

from api.api_v1 import auth, goods, utils


api_v1_router = APIRouter()
api_v1_router.include_router(auth.router, prefix="/admin/auth", tags=["用户"])
api_v1_router.include_router(goods.router, prefix="/admin/goods", tags=["商品"])
api_v1_router.include_router(utils.router, prefix="/admin/utils", tags=["工具类"])
