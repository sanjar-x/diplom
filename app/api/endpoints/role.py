from typing import List
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status
from ..dependencies.database_session import get_session
from ...schemas.role import RoleCreate, RoleResponse
from ...models.models import Role


router = APIRouter(prefix="/roles")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=RoleResponse)
async def create_role(
    payload: RoleCreate,
    db_session: AsyncSession = Depends(get_session),
):
    role: Role = Role(**payload.model_dump())
    await role.save(db_session)
    return role


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[RoleResponse])
async def get_roles(db_session: AsyncSession = Depends(get_session)):

    roles: List[Role] = await Role().find_all(db_session)
    return roles


# @router.get("/", status_code=status.HTTP_200_OK, response_model=RoleResponse)
# async def get_role(role_id: str, db_session: AsyncSession = Depends(get_session)):
#     role: Role | None = await Role().find(db_session, [Role.role_id == role_id])
#     return role
