import logging

from fastapi import APIRouter, Body, Query
from tortoise.expressions import Q

from app.controllers.user import user_controller
from app.schemas.base import Fail, Success, SuccessExtra
from app.schemas.users import *

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/list", summary="Liset users")
async def list_user(
    page: int = Query(1, description="Page number"),
    page_size: int = Query(10, description="Page size"),
    username: str = Query("", description="Username"),
    email: str = Query("", description="Email"),
):
    q = Q()
    if username:
        q &= Q(username__contains=username)
    if email:
        q &= Q(email__contains=email)
    total, user_objs = await user_controller.list(page=page, page_size=page_size, search=q)
    data = [await obj.to_dict(m2m=True, exclude_fields=["password"]) for obj in user_objs]

    return SuccessExtra(data=data, total=total, page=page, page_size=page_size)


@router.get("/get", summary="Get user by ID")
async def get_user(
    user_id: int = Query(..., description="User ID"),
):
    user_obj = await user_controller.get(id=user_id)
    user_dict = await user_obj.to_dict(exclude_fields=["password"])
    return Success(data=user_dict)


@router.post("/create", summary="Create user")
async def create_user(
    user_in: UserCreate,
):
    user = await user_controller.get_by_email(user_in.email)
    if user:
        return Fail(code=400, msg="The user with this email already exists in the system.")
    await user_controller.create_user(obj_in=user_in)
    return Success(msg="Created Successfully")


@router.post("/update", summary="Update user")
async def update_user(
    user_in: UserUpdate,
):
    await user_controller.update(id=user_in.id, obj_in=user_in)
    return Success(msg="Updated Successfully")


@router.delete("/delete", summary="Delete user")
async def delete_user(
    user_id: int = Query(..., description="User ID"),
):
    await user_controller.remove(id=user_id)
    return Success(msg="Deleted Successfully")


@router.post("/reset_password", summary="Reset user password")
async def reset_password(user_id: int = Body(..., description="User ID", embed=True)):
    await user_controller.reset_password(user_id)
    return Success(msg="Success reset to 123456")
