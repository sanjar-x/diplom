from typing import List
from uuid import UUID
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException, status
from ..dependencies.database_session import get_session
from ...schemas.department import (
    DepartmentCreate,
    DepartmentResponse,
    DepartmentFullResponse,
)
from ...models.models import Department


router = APIRouter(prefix="/departments")


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=DepartmentResponse
)
async def create_department(
    payload: DepartmentCreate,
    session: AsyncSession = Depends(get_session),
):
    department: Department = Department(**payload.model_dump())
    await department.save(session)
    return department


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[DepartmentFullResponse]
)
async def get_departments(session: AsyncSession = Depends(get_session)):
    departments: List[Department] = await Department().find_all_with(
        session, [joinedload(Department.faculty)]
    )
    return departments


@router.patch("/switch", status_code=status.HTTP_201_CREATED)
async def switch_status(
    department_id: UUID,
    active: bool,
    session: AsyncSession = Depends(get_session),
):
    department: Department | None = await Department().find(
        session, [Department.department_id == department_id]
    )
    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Department with ID {department_id} not exist",
        )

    await department.update(session, active=active)
    return {"message": f"Status switched to {active}"}


@router.delete("/", status_code=status.HTTP_200_OK)
async def delet_department(
    department_id,
    session: AsyncSession = Depends(get_session),
):
    department: Department | None = await Department().find(
        session, [Department.department_id == department_id]
    )
    if department:
        await department.delete(session)
    return {"message": "department deleted"}
