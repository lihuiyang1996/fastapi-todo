from app.controllers.user import user_controller, UserCreate
from app.controllers.api import api_controller
from app.models.admin import Role, Api
from tortoise.expressions import Q
from app.log import logger

async def init_superuser():
    if not await user_controller.model.exists():
        logger.info("Creating default superuser...")
        await user_controller.create_user(
            UserCreate(
                username="admin",
                email="admin@admin.com",
                password="123456",
                is_active=True,
                is_superuser=True,
            )
        )

async def init_apis():
    if not await api_controller.model.exists():
        logger.info("Refreshing API list...")
        await api_controller.refresh_api()

async def init_roles():
    if not await Role.exists():
        logger.info("Creating roles: 管理员 / 普通用户")
        admin_role = await Role.create(name="管理员", desc="管理员角色")
        user_role = await Role.create(name="普通用户", desc="普通用户角色")

        all_apis = await Api.all()
        await admin_role.apis.add(*all_apis)

        basic_apis = await Api.filter(Q(method__in=["GET"]) | Q(tags="基础模块"))
        await user_role.apis.add(*basic_apis)