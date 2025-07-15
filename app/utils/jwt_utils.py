import jwt

from app.schemas.login import JWTPayload
from app.settings.config import get_config

config = get_config()


def create_access_token(*, data: JWTPayload):
    payload = data.model_dump().copy()
    encoded_jwt = jwt.encode(payload, config.SECRET_KEY, algorithm=config.JWT_ALGORITHM)
    return encoded_jwt
