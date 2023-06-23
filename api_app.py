from fastapi import FastAPI, Depends
from database.connector import get_db
from database.models import Currency
from schemas.schema import CurrencySchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime


# FASTAPI
app = FastAPI()


@app.get("/")
async def root():
    return {
        "msg": "Welcome to the Digital Currency API, for the docs go to the route /docs"
    }


@app.get("/currency-all-info")
async def get_currency_history(ticker_name: str, db: AsyncSession = Depends(get_db)):
    query = select(Currency).where(Currency.instrument_name == ticker_name)
    results = await db.execute(query)
    data = results.scalars().all()
    # print(data)
    return {"result": data}


@app.get("/currency-price")
async def get_currency_price(ticker_name: str, db: AsyncSession = Depends(get_db)):
    query = select(Currency).where(Currency.instrument_name == ticker_name)
    results = await db.execute(query)
    data = results.scalars().first()
    return {"result": {"ticker_name": ticker_name, "current_price": data.current_value}}


@app.get("/currency-by-date")
async def get_currency_history_by_date(
    ticker_name: str, dt: str, db: AsyncSession = Depends(get_db)
):
    date = datetime.strptime(dt, "%Y-%m-%d").date()
    query = select(Currency).where(Currency.instrument_name == ticker_name)
    results = await db.execute(query)
    data = results.scalars().all()
    output = []
    for curr in data:
        dt = datetime.fromtimestamp(curr.timestamp / 1000).date()
        if dt == date:
            output.append(curr)
    return {"date": date, "result": output}
