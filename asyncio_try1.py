import asyncio


async def delay(seconds):

    print(f"start sleeping for {seconds} seconds")
    await asyncio.sleep(seconds)
    print(f"finished sleeping for {seconds} seconds")

    return seconds


async def main1():

    await delay(3)
    a = 1 + 3
    print(f"this is the value of {a}")

    await delay(5)


async def main2():

    sleep_for_three = asyncio.create_task(delay(3))

    result = await sleep_for_three
    a = 1 + 3
    print(f"this is the value of {a}")
    print(result)


async def main3():

    sleep_for_three = asyncio.create_task(delay(3))
    sleep_for_five = asyncio.create_task(delay(5))

    await sleep_for_three
    await sleep_for_five
    a = 1 + 3
    print(f"this is the value of {a}")


async def main4():

    sleep_for_three = asyncio.create_task(delay(3))
    print("done")


async def hello_every_second():
    for i in range(3):
        print(f"hello {i}")
        await asyncio.sleep(1)


async def main5():

    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))

    await hello_every_second()

    await first_delay
    await second_delay


asyncio.run(main5())
