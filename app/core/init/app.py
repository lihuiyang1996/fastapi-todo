from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from app.api import api_router
from app.settings.config import get_config
from app.core.exceptions import (
    DoesNotExist, DoesNotExistHandle,
    HTTPException, HttpExcHandle,
    IntegrityError, IntegrityHandle,
    RequestValidationError, RequestValidationHandle,
    ResponseValidationError, ResponseValidationHandle,
)
from app.core.middlewares import BackGroundTaskMiddleware, HttpAuditLogMiddleware

from app.core.init.db import init_db
from app.core.init.seed import init_superuser, init_apis, init_roles

config = get_config()

def make_middlewares() -> list[Middleware]:
    return [
        Middleware(CORSMiddleware,
            allow_origins=config.CORS_ORIGINS,
            allow_credentials=config.CORS_ALLOW_CREDENTIALS,
            allow_methods=config.CORS_ALLOW_METHODS,
            allow_headers=config.CORS_ALLOW_HEADERS,
        ),
        Middleware(BackGroundTaskMiddleware),
        Middleware(HttpAuditLogMiddleware,
            methods=["GET", "POST", "PUT", "DELETE"],
            exclude_paths=["/api/v1/base/access_token", "/docs", "/openapi.json"],
        ),
    ]

def register_exceptions(app: FastAPI):
    app.add_exception_handler(DoesNotExist, DoesNotExistHandle)
    app.add_exception_handler(HTTPException, HttpExcHandle)
    app.add_exception_handler(IntegrityError, IntegrityHandle)
    app.add_exception_handler(RequestValidationError, RequestValidationHandle)
    app.add_exception_handler(ResponseValidationError, ResponseValidationHandle)

def register_routers(app: FastAPI, prefix: str = "/api"):
    app.include_router(api_router, prefix=prefix)

async def init_data():
    await init_db()
    await init_superuser()
    await init_apis()
    await init_roles()