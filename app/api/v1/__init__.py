from fastapi import APIRouter

from .users import users_router
from .base import base_router
from .roles import roles_router
from .apis import apis_router
from .auditlog import auditlog_router

from app.core.dependency import DependPermission

v1_router = APIRouter()

v1_router.include_router(base_router, prefix="/base")
v1_router.include_router(users_router, prefix="/user", dependencies=[DependPermission])
v1_router.include_router(roles_router, prefix="/role", dependencies=[DependPermission])
v1_router.include_router(apis_router, prefix="/api", dependencies=[DependPermission])
v1_router.include_router(auditlog_router, prefix="/auditlog", dependencies=[DependPermission])