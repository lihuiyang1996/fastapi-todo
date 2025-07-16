import contextvars

from app.models.admin import User
from starlette.background import BackgroundTasks

CTX_USER: contextvars.ContextVar[User] = contextvars.ContextVar("user", default=0)
CTX_BG_TASKS: contextvars.ContextVar[BackgroundTasks] = contextvars.ContextVar("bg_task", default=None)
