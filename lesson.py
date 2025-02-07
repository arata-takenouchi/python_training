import asyncio
import multiprocessing
import threading
import time
import requests
import aiohttp

loop = asyncio.get_event_loop()

# async def hello(url):
#     print(requests.get(url).content)
#     print(time.time())

async def hello(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            print(requests.get(url).content)
            print(time.time())
    await asyncio.sleep(10)

loop.run_until_complete(asyncio.wait([
    hello("http://httpbin.org/headers"),
    hello("http://httpbin.org/headers")
]))
