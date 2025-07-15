from fastapi import APIRouter
from .users import users_router
from .base import base_router

v1_router = APIRouter()

v1_router.include_router(base_router, prefix="/base")
v1_router.include_router(users_router, prefix="/user")
