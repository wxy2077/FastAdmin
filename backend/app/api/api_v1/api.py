from fastapi import APIRouter

from api.api_v1 import goods


api_v1_router = APIRouter()
api_v1_router.include_router(goods.router, prefix="/auth", tags=["用户"])
