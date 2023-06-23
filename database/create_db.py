from .connector import create_db
from .models import (
    Currency,
)  # important for creating the database when running create_db
import asyncio


def init_db():
    asyncio.run(create_db())
