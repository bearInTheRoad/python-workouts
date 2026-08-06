import asyncio


async def main():
    await asyncio.sleep(3)
    print("Waited for 3 seconds")


def main2():
    print("called main2")
    print("Waited for 1 seconds")


loop = asyncio.new_event_loop()
loop.call_soon(main2)
loop.run_until_complete(main())

# this_loop = asyncio.get_running_loop()
