from typing import List
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status
from ..dependencies.database_session import get_session
from ...schemas.user import UserCreate, UserResponse
from ...models.models import User


router = APIRouter(prefix="/users")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(
    payload: UserCreate,
    db_session: AsyncSession = Depends(get_session),
):
    user: User = User(**payload.model_dump())
    await user.save(db_session)
    return user


@router.get("/", status_code=status.HTTP_200_OK)
async def get_users(
    db_session: AsyncSession = Depends(get_session),
):
    return await User().find_all_with(db_session, options=[joinedload(User.role)])
