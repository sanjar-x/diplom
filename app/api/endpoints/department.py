from typing import List
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status
from ..dependencies.database_session import get_session
from ...schemas.department import DepartmentCreate, DepartmentResponse
from ...models.models import Department


router = APIRouter(prefix="/departments")


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=DepartmentResponse
)
async def create_department(
    payload: DepartmentCreate,
    db_session: AsyncSession = Depends(get_session),
):
    department: Department = Department(**payload.model_dump())
    await department.save(db_session)
    return department


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[DepartmentResponse]
)
async def get_departments(db_session: AsyncSession = Depends(get_session)):
    departments: List[Department] = await Department().find_all_with(
        db_session, [joinedload(Department.faculty)]
    )
    return departments
