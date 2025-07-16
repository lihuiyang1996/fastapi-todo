from fastapi import APIRouter

from .todo import router

todo_router = APIRouter()
todo_router.include_router(router, tags=["TODO 模块"])

__all__ = ["todo_router"]
