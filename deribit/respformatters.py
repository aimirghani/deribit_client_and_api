from abc import ABC, abstractmethod


class IRespFormatter(ABC):
    @abstractmethod
    def format(self):
        pass


class TickerFormatter(IRespFormatter):
    def format(self, resp):
        return {
            "instrument_name": resp["result"]["instrument_name"],
            "current_value": resp["result"]["last_price"],
            "timestamp": resp["result"]["timestamp"],
        }
