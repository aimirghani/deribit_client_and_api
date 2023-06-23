from pydantic.dataclasses import dataclass


@dataclass
class CurrencySchema:
    instrument_name: str
    current_value: float
    timestamp: int
