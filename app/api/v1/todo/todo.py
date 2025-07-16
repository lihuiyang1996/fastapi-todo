import logging
from fastapi import APIRouter, Query, Body, Depends
from tortoise.expressions import Q

from app.controllers.todo import todo_controller
from app.core.dependency import DependAuth
from app.schemas.base import Success, SuccessExtra
from app.schemas.todo import TodoCreate, TodoUpdate
from app.core.ctx import CTX_USER_ID

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/list", summary="List my todos")
async def list_todos(
    page: int = Query(1, description="Page number"),
    page_size: int = Query(10, description="Page size"),
    title: str = Query("", description="Search by title"),
):
    user_id = CTX_USER_ID.get()
    q = Q(user_id=user_id)
    if title:
        q &= Q(title__icontains=title)
    total, todos = await todo_controller.list(page=page, page_size=page_size, search=q)
    data = [await todo.to_dict() for todo in todos]
    return SuccessExtra(data=data, total=total, page=page, page_size=page_size)


@router.get("/get", summary="Get a todo by ID")
async def get_todo(todo_id: int = Query(..., description="Todo ID"),):
    user_id = CTX_USER_ID.get()
    todo = await todo_controller.get_user_todo(todo_id=todo_id, user_id=user_id)
    return Success(data=await todo.to_dict())


@router.post("/create", summary="Create todo")
async def create_todo(todo_in: TodoCreate,):
    user_id = CTX_USER_ID.get()
    await todo_controller.create_for_user(user_id=user_id, todo_in=todo_in)
    return Success(msg="Created Successfully")


@router.post("/update", summary="Update todo")
async def update_todo(todo_in: TodoUpdate,):
    user_id = CTX_USER_ID.get()
    await todo_controller.update_user_todo(
        todo_id=todo_in.id, user_id=user_id, todo_in=todo_in
    )
    return Success(msg="Updated Successfully")


@router.delete("/delete", summary="Delete todo")
async def delete_todo(todo_id: int = Query(..., description="Todo ID"),):
    user_id = CTX_USER_ID.get()
    await todo_controller.delete_user_todo(todo_id=todo_id, user_id=user_id)
    return Success(msg="Deleted Successfully")