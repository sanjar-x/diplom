from typing import List
from uuid import UUID
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException, status
from ..dependencies.database_session import get_session
from ...schemas.faculty import FacultyCreate, FacultyResponse
from ...models.models import Faculty


router = APIRouter(prefix="/faculties")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FacultyResponse)
async def create_faculty(
    payload: FacultyCreate,
    session: AsyncSession = Depends(get_session),
):
    faculty: Faculty = Faculty(**payload.model_dump())
    await faculty.save(session)
    return faculty


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[FacultyResponse])
async def get_faculties(session: AsyncSession = Depends(get_session)):
    faculties: List[Faculty] = await Faculty().find_all(session)
    return faculties


@router.patch("/switch", status_code=status.HTTP_201_CREATED)
async def switch_status(
    faculty_id: UUID,
    active: bool,
    session: AsyncSession = Depends(get_session),
):
    faculty: Faculty | None = await Faculty().find(
        session, [Faculty.faculty_id == faculty_id]
    )
    if not faculty:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Faculty with ID {faculty_id} not exist",
        )

    await faculty.update(session, active=active)
    return {"message": f"Status switched to {active}"}


@router.delete("/", status_code=status.HTTP_200_OK)
async def delet_faculty(
    faculty_id,
    session: AsyncSession = Depends(get_session),
):
    faculty: Faculty | None = await Faculty().find(
        session, [Faculty.faculty_id == faculty_id]
    )
    if faculty:
        await faculty.delete(session)
    return {"message": "faculty deleted"}
