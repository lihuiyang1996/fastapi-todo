from fastapi import FastAPI
from app.settings.config import get_config
from contextlib import asynccontextmanager
from app.core.init.app import (
    make_middlewares,
    register_exceptions,
    register_routers,
)
from app.core.init.db import connect_db, close_db

config = get_config()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await close_db()


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