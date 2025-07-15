from fastapi import FastAPI
from tortoise import Tortoise
from app.settings.config import get_config
from contextlib import asynccontextmanager
from app.core.init_app import (
    init_data,
    make_middlewares,
    register_exceptions,
    register_routers,
)

config = get_config()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_data()
    yield
    await Tortoise.close_connections()


def create_app() -> FastAPI:
    app = FastAPI(
        title=config.APP_TITLE,
        description=config.APP_DESCRIPTION,
        version=config.VERSION,
        openapi_url="/openapi.json",
        middleware=make_middlewares(),
        lifespan=lifespan,
    )
    register_exceptions(app)
    register_routers(app, prefix="/api")
    return app


app = create_app()