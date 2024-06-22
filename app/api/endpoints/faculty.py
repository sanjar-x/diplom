from typing import List
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status
from ..dependencies.database_session import get_session
from ...schemas.faculty import FacultyCreate, FacultyResponse
from ...models.models import Faculty


router = APIRouter(prefix="/faculties")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FacultyResponse)
async def create_faculty(
    payload: FacultyCreate,
    db_session: AsyncSession = Depends(get_session),
):
    faculty: Faculty = Faculty(**payload.model_dump())
    await faculty.save(db_session)
    return faculty


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[FacultyResponse])
async def get_faculties(db_session: AsyncSession = Depends(get_session)):
    faculties: List[Faculty] = await Faculty().find_all(db_session)
    return faculties
