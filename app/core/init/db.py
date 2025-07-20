import shutil
from aerich import Command
from app.settings.config import get_config
from tortoise import Tortoise
from app.log import logger

config = get_config()

async def init_db():
    command = Command(tortoise_config=config.TORTOISE_ORM)
    try:
        await command.init_db(safe=True)
    except FileExistsError:
        logger.info("Migrations already exist.")

    await command.init()
    try:
        await command.migrate()
    except AttributeError:
        logger.warning("Model history not found, resetting migrations...")
        shutil.rmtree("migrations", ignore_errors=True)
        await command.init_db(safe=True)

    await command.upgrade(run_in_transaction=True)

async def connect_db():
    await Tortoise.init(config=config.TORTOISE_ORM)

async def close_db():
    await Tortoise.close_connections()