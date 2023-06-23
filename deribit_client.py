from deribit.client import DeribitClient
from deribit.respformatters import TickerFormatter
from deribit.scheduler import Scheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database.connector import SessionLocal
from database.models import Currency


msg = {
    "jsonrpc": "2.0",
    "id": 8106,
    "method": "public/ticker",
    "params": {"instrument_name": "BTC_USDC"},
}


def ticker_params_generator(ticker_name):
    return {"instrument_name": ticker_name}


def run_deribit_client():
    drbt_clnt = DeribitClient(msg=msg, db_connector=SessionLocal, db_model=Currency)

    params_list = [
        ticker_params_generator(ticker) for ticker in ["BTC_USDC", "ETH_USDC"]
    ]

    sched = Scheduler(sched_type=AsyncIOScheduler)
    sched.run(drbt_clnt.call_many, period=3, args=[params_list, TickerFormatter()])


if __name__ == "__main__":
    run_deribit_client()
