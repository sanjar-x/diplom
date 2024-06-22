from typing import Annotated
from pydantic import SecretStr
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ..dependencies.database_session import get_session
from ...schemas.user import TokenResponse
from ...models.models import User
from ...services.auth import create_access_token


router = APIRouter(prefix="/auth")


@router.post(
    "/token", status_code=status.HTTP_201_CREATED, response_model=TokenResponse
)
async def get_token_for_user(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db_session: AsyncSession = Depends(get_session),
):
    user: User | None = await User.find(
        db_session, [User.phone_number == form_data.username]
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    if not user.check_password(SecretStr(form_data.password)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Password is incorrect"
        )
    token = await create_access_token(user)
    return {"access_token": token, "token_type": "bearer"}
