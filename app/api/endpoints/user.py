from typing import List
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException, status
from ..dependencies.database_session import get_session
from ...schemas.user import UserCreate, UserResponse, UserUpdate
from ...models.models import Role, User


router = APIRouter(prefix="/users")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(
    payload: UserCreate,
    session: AsyncSession = Depends(get_session),
):
    role: Role | None = await Role().find(session, [Role.name == payload.role_name])
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Role {payload.role_name} not exist",
        )

    exist_user: User | None = await User().find(
        session, [User.phone_number == payload.phone_number]
    )
    if exist_user:
        raise HTTPException(
            status_code=status.HTTP_226_IM_USED,
            detail=f"User with phone number {exist_user.phone_number} already exist",
        )
    user: User = User(**payload.model_dump(exclude={"role_name"}), role_id=role.role_id)
    user = await user.save(session)
    return user


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[UserResponse])
async def get_users(
    session: AsyncSession = Depends(get_session),
):
    return await User().find_all_with(session, options=[joinedload(User.role)])


# @router.patch("/", status_code=status.HTTP_201_CREATED)
# async def update_user(
#     payload: UserUpdate,
#     session: AsyncSession = Depends(get_session),
# ):
#     user: User | None = await User().find(session, [User.user_id == payload.user_id])
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"User with ID {payload.user_id} not exist",
#         )
#     role: Role | None = await Role().find(session, [Role.name == payload.role_name])
#     if not role:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Role {payload.role_name} not exist",
#         )

#     await user.update(
#         session,
#         **payload.model_dump(exclude={"role_name"}),
#         exclude_none=True,
#         role_id=role.role_id,
#     )
#     return user


@router.delete("/", status_code=status.HTTP_200_OK)
async def delet_user(
    user_id,
    session: AsyncSession = Depends(get_session),
):
    user: User | None = await User().find(session, [User.user_id == user_id])
    if user:
        await user.delete(session)
    return {"message": "user deleted"}
