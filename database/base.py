from sqlalchemy import BIGINT
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    type_annotation_map = {int: BIGINT}
