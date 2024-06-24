from typing import List
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status
from ..dependencies.database_session import get_session
from ...schemas.employees import EmployeeCreate, EmployeeResponse, EmployeeFullResponse
from ...models.models import Employee

router = APIRouter(prefix="/employees")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=EmployeeResponse)
async def create_employee(
    payload: EmployeeCreate,
    db_session: AsyncSession = Depends(get_session),
):
    employee: Employee = Employee(**payload.model_dump())
    await employee.save(db_session)
    return employee


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[EmployeeFullResponse]
)
async def get_employees(db_session: AsyncSession = Depends(get_session)):
    employees = await Employee().find_all_with(
        db_session,
        [
            joinedload(Employee.user),
            joinedload(Employee.division),
            joinedload(Employee.department),
        ],
    )
    return employees
