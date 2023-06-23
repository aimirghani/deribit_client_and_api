from .base import Base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv, find_dotenv
from os import getenv

env_file = find_dotenv()
load_dotenv(env_file)

DB_USER = getenv("DB_USER")
DB_PASS = getenv("DB_PASS")
BD_HOST = getenv("BD_HOST")
DB_NAME = getenv("DB_NAME")
DB_PORT = getenv("DB_PORT")

DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{BD_HOST}:{DB_PORT}/{DB_NAME}"

# engine = create_async_engine(
#     "sqlite+aiosqlite:///db.sqlite3", connect_args={"check_same_thread": False}
# )

engine = create_async_engine(url=DB_URL, poolclass=NullPool)
SessionLocal = async_sessionmaker(engine)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
