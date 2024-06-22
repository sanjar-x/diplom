from datetime import datetime, timedelta, timezone

from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from jose.exceptions import JWTError, ExpiredSignatureError

import os
from app.models.models import User


async def verify_jwt(token: str) -> str:
    try:
        decoded_token = jwt.decode(
            token=token,
            key=os.getenv("KEY"),  # type: ignore
        )

        return decoded_token["sub"]

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="HTTP_401_UNAUTHORIZED"
        )
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="HTTP_401_UNAUTHORIZED",
        )


class AuthBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials | None = await super().__call__(
            request
        )
        if not credentials:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")
        if credentials.scheme != "Bearer":
            raise HTTPException(
                status_code=403, detail="Invalid authentication scheme."
            )
        if not await verify_jwt(credentials.credentials):
            raise HTTPException(
                status_code=403, detail="Invalid token or expired token."
            )
        return credentials.credentials


async def create_access_token(user: User) -> str:
    payload = {
        "sub": user.phone_number,
        "exp": datetime.now(timezone.utc) + timedelta(days=30),
        "iss": "algoritm",
    }
    try:
        token = jwt.encode(payload, os.getenv("KEY"))  # type: ignore
        return token
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="HTTP_401_UNAUTHORIZED"
        )
