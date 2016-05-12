# -*- coding: utf-8 -*-
import asyncio
from datetime import datetime, timedelta
import requests


async def get_async():
    async with requests.get("http://www.varzesh3.com") as r:
        return await r.content


async def main():

    captured_time = datetime.now()
    result = await asyncio.gather(*[asyncio.Task(get_async()) for u in range(1, 100)], return_exceptions=True)

    # result = [requests.get(u).content for u in urls]

    total_time = (datetime.now() - captured_time)
    print("Total time: %ss" % (total_time))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    # with aiohttp.ClientSession(loop=loop) as session:

