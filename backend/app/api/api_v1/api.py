from fastapi import APIRouter

from app.api.api_v1 import auth

api_v1_router = APIRouter()
api_v1_router.include_router(auth.router, prefix="/auth", tags=["users"])
