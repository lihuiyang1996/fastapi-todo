from functools import lru_cache
import os
import typing

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # JWT
    SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int

    # DB
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    VERSION: str = "0.1.0"
    APP_TITLE: str = "Todo FastAPI"
    PROJECT_NAME: str = "Todo FastAPI"
    APP_DESCRIPTION: str = "Description"

    CORS_ORIGINS: typing.List = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: typing.List = ["*"]
    CORS_ALLOW_HEADERS: typing.List = ["*"]

    DEBUG: bool = True

    PROJECT_ROOT: str = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    BASE_DIR: str = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir))
    LOGS_ROOT: str = os.path.join(BASE_DIR, "app/logs")
    @property
    def TORTOISE_ORM(self) -> dict:
        return {
            "connections": {
                # SQLite configuration
                # "sqlite": {
                #     "engine": "tortoise.backends.sqlite",
                #     "credentials": {"file_path": f"{BASE_DIR}/db.sqlite3"},  # Path to SQLite database file
                # },
                # MySQL/MariaDB configuration
                # Install with: tortoise-orm[asyncmy]
                # "mysql": {
                #     "engine": "tortoise.backends.mysql",
                #     "credentials": {
                #         "host": "localhost",  # Database host address
                #         "port": 3306,  # Database port
                #         "user": "yourusername",  # Database username
                #         "password": "yourpassword",  # Database password
                #         "database": "yourdatabase",  # Database name
                #     },
                # },
                # PostgreSQL configuration
                # Install with: tortoise-orm[asyncpg]
                "postgres": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "host": self.DB_HOST,  # Database host address
                        "port": self.DB_PORT,  # Database port
                        "user": self.DB_USER,  # Database username
                        "password": self.DB_PASSWORD,  # Database password
                        "database": self.DB_NAME,  # Database name
                    },
                },
                # MSSQL/Oracle configuration
                # Install with: tortoise-orm[asyncodbc]
                # "oracle": {
                #     "engine": "tortoise.backends.asyncodbc",
                #     "credentials": {
                #         "host": "localhost",  # Database host address
                #         "port": 1433,  # Database port
                #         "user": "yourusername",  # Database username
                #         "password": "yourpassword",  # Database password
                #         "database": "yourdatabase",  # Database name
                #     },
                # },
                # SQLServer configuration
                # Install with: tortoise-orm[asyncodbc]
                # "sqlserver": {
                #     "engine": "tortoise.backends.asyncodbc",
                #     "credentials": {
                #         "host": "localhost",  # Database host address
                #         "port": 1433,  # Database port
                #         "user": "yourusername",  # Database username
                #         "password": "yourpassword",  # Database password
                #         "database": "yourdatabase",  # Database name
                #     },
                # },
            },
            "apps": {
                "models": {
                    "models": ["app.models", "aerich.models"],
                    "default_connection": "postgres",
                },
            },
            "use_tz": False,  # Whether to use timezone-aware datetimes
            "timezone": "Asia/Shanghai",  # Timezone setting
    }
    DATETIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"


@lru_cache()
def get_config() -> Settings:
    return Settings()  # type: ignore[call-arg]