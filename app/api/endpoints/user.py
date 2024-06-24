from typing import List
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException, status
from ..dependencies.database_session import get_session
from ...schemas.user import UserCreate, UserResponse
from ...models.models import Role, User


router = APIRouter(prefix="/users")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    payload: UserCreate,
    session: AsyncSession = Depends(get_session),
):
    role: Role | None = await Role().find(session, [Role.name == payload.role_name])
    if not role:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Role {payload.role_name} not exist",
        )

    user: User = User(**payload.model_dump(exclude={"role_name"}), role_id=role.role_id)
    user = await user.save(session)
    return user


@router.get("/", status_code=status.HTTP_200_OK)
async def get_users(
    db_session: AsyncSession = Depends(get_session),
):
    return await User().find_all_with(db_session, options=[joinedload(User.role)])
