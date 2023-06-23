import pytest
from httpx import AsyncClient
from api_app import app


@pytest.mark.asyncio
async def test_currency_all_info():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(
            "/currency-all-info", params={"ticker_name": "BTC_USDC"}
        )
    assert response.status_code == 200
    assert type(response.json()["result"]) == list


@pytest.mark.asyncio
async def test_currency_price():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/currency-price", params={"ticker_name": "ETH_USDC"})
    assert response.status_code == 200
    assert response.json() == {
        "result": {"ticker_name": "ETH_USDC", "current_price": 1778.22}
    }


@pytest.mark.asyncio
async def test_currency_info_by_date():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(
            "/currency-by-date", params={"ticker_name": "BTC_USDC", "dt": "2023-06-23"}
        )
    assert response.status_code == 200
    assert response.json()["date"] == "2023-06-23"
