import asyncio
import time

loop =  asyncio.get_event_loop()

class AwaitableClass(object):
    def __init__(self, name, loop):
        self.name = name
        self.loop = loop

    def __await__(self):
        reader, writer = yield from asyncio.open_connection(
            '127.0.0.1', 8888, loop=loop)
        writer.write(self.name.encode())
        writer.write_eof()
        data = yield from reader.read()
        data = int(data.decode())
        return data

class AsyncIterater(object):
    def __init__(self, name, loop):
        self.name = name
        self.loop = loop

    def __aiter__(self):
        return self

    async def __anext__(self):
        data = await AwaitableClass(self.name, self.loop)
        if data < 0:
            raise StopAsyncIteration
        return data

class AsyncContextManager(object):
    def __init__(self, name, loop):
        self.enter = 'enter'
        self.ac = AsyncIterater(name, loop)
        self.exit = 'exit'

    async def __aenter__(self):
        print(self.enter)
        await asyncio.sleep(3)
        return self.ac

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(self.exit)
        await asyncio.sleep(3)

import time
import concurrent.futures
def blocking_task(name):
    print(f'block {name}')
    time.sleep(1)
    return f'done {name}'

async def main(name, loop):
    # print('chunk reader')
    # result = await AwaitableClass(name, loop)
    # async with AsyncContextManager(name, loop) as ac:
    #     async for i in ac:
    #         print(i)
    def done_callback(future):
        print(future.result())
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=5)
    for i in range(4):
        future = loop.run_in_executor(executor, blocking_task, name)
        future.add_done_callback(done_callback)
    executor.shutdown(wait=True)

loop.run_until_complete(asyncio.wait([
    main('task1', loop), main('task2', loop)
]))
loop.close()
