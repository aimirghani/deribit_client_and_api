from sqlalchemy.orm import Mapped, mapped_column

# from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from .base import Base


class Currency(Base):
    __tablename__ = "currencies"
    id: Mapped[int] = mapped_column(primary_key=True)
    instrument_name: Mapped[str] = mapped_column(nullable=False)
    current_value: Mapped[float] = mapped_column(nullable=False)
    timestamp: Mapped[int] = mapped_column(nullable=False)

    @property
    def date(self):
        return self.date_

    @date.setter
    def date(self):
        self.date_ = datetime.fromtimestamp(self.timestamp / 1000).date()
