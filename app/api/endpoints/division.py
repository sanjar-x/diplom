from typing import List
from uuid import UUID
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException, status
from ..dependencies.database_session import get_session
from ...schemas.division import DivisionCreate, DivisionResponse
from ...models.models import Division


router = APIRouter(prefix="/divisions")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=DivisionResponse)
async def create_division(
    payload: DivisionCreate,
    session: AsyncSession = Depends(get_session),
):
    division: Division = Division(**payload.model_dump())
    await division.save(session)
    return division


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[DivisionResponse])
async def get_divisions(session: AsyncSession = Depends(get_session)):
    divisions = await Division().find_all(session)
    return divisions


@router.patch("/switch", status_code=status.HTTP_201_CREATED)
async def switch_status(
    division_id: UUID,
    active: bool,
    session: AsyncSession = Depends(get_session),
):
    division: Division | None = await Division().find(
        session, [Division.division_id == division_id]
    )
    if not division:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Department with ID {division_id} not exist",
        )

    await division.update(session, active=active)
    return {"message": f"Status switched to {active}"}


@router.delete("/", status_code=status.HTTP_200_OK)
async def delet_division(
    division_id,
    session: AsyncSession = Depends(get_session),
):
    division: Division | None = await Division().find(
        session, [Division.division_id == division_id]
    )
    if division:
        await division.delete(session)
    return {"message": "division deleted"}
