from typing import List
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status
from ..dependencies.database_session import get_session
from ...schemas.division import DivisionCreate, DivisionResponse
from ...models.models import Division


router = APIRouter(prefix="/divisions")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=DivisionResponse)
async def create_division(
    payload: DivisionCreate,
    db_session: AsyncSession = Depends(get_session),
):
    division: Division = Division(**payload.model_dump())
    await division.save(db_session)
    return division


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[DivisionResponse])
async def get_divisions(db_session: AsyncSession = Depends(get_session)):
    faculties = await Division().find_all(db_session)
    return faculties


@router.delete("/", status_code=status.HTTP_200_OK)
async def delet_division(
    division_id,
    db_session: AsyncSession = Depends(get_session),
):
    division: Division | None = await Division().find(
        db_session, [Division.division_id == division_id]
    )
    if division:
        await division.delete(db_session)
    return {"message": "division deleted"}
