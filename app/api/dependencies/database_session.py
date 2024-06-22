from typing import AsyncGenerator

from sqlalchemy.engine import make_url
from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker

engine = create_async_engine(
    url=make_url(
        name_or_url="postgresql+asyncpg://root:iam3489495@localhost:5432/test"
    ),
    echo=True,
    future=True,
)

async_session = async_sessionmaker(engine, autoflush=False, expire_on_commit=False)


async def get_session() -> AsyncGenerator:
    async with async_session() as session:
        yield session
