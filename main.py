from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers import api_router

app = FastAPI(
    title="Отдел Кадров",
    description="API-документация для Отдела кадров",
    version="0.0.1",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

import asyncio
from app.api.dependencies.database_session import engine
from app.models.models import Base


async def reset_database():
    async with engine.begin() as connection:

        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(reset_database())
