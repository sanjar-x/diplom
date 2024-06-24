from fastapi import APIRouter
from app.api.dependencies.database_session import engine
from app.models.models import Base

router = APIRouter(prefix="/settings")


@router.get("/reset-db")
async def get_token_for_user():
    async with engine.begin() as connection:

        await connection.exec_driver_sql("DROP SCHEMA public CASCADE")
        await connection.exec_driver_sql("CREATE SCHEMA public")
        await connection.run_sync(Base.metadata.create_all)
    return {"message": "Reseted"}
