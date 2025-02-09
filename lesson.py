import asyncio

loop = asyncio.get_event_loop()

async def main():
    print('start')
    await asyncio.sleep(3)
    print('done')

loop.run_until_complete(main())
loop.close()
