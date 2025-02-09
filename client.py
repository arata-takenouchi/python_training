import asyncio

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

async def main(name, loop):
    print('chunk reader')
    result = await AwaitableClass(name, loop)
    print(result)

message = 'Hello World!'
loop.run_until_complete(asyncio.wait([
    main('task1', loop), main('task2', loop)
]))
loop.close()
