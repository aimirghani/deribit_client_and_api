import aiohttp
import asyncio
from pprint import pprint


class DeribitClient:
    def __init__(self, msg, db_connector=None, db_model=None) -> None:
        self.url = "wss://test.deribit.com/ws/api/v2"
        self.msg = msg
        self.db_connector = db_connector
        self.db_model = db_model

    async def prepare_request_coro(self, params, formatter=None):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect(url=self.url) as ws:
                self.msg["params"] = params
                await ws.send_json(self.msg)
                resp = await ws.receive_json()
                result = formatter.format(resp) if formatter is not None else resp
            pprint(result)
            return result

    async def _persist_to_db(self, data):
        if self.db_connector is not None:
            async with self.db_connector() as session:
                async with session.begin():
                    db_entry = self.db_model(**data)
                    session.add(db_entry)
                    await session.commit()
        else:
            raise ValueError("No db session constructor has been provided.")

    async def call_once(self, params, formatter=None):
        resp = await self.prepare_request_coro(params, formatter)
        if self.db_connector is not None:
            await self._persist_to_db(resp)
        return resp

    async def call_many(self, params_list, formatter=None):
        tasks = []
        for params in params_list:
            tasks.append(asyncio.create_task(self.call_once(params, formatter)))
        resp = await asyncio.gather(*tasks)
        return resp
