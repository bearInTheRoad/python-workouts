import asyncio
from asyncio import CancelledError, TimeoutError
from asyncio_try1 import delay


async def main1():
    long_task = asyncio.create_task(delay(10))

    seconds_elapsed = 0

    while not long_task.done():
        print("Task not finisshed, checking again in 1 second")

        await asyncio.sleep(1)

        seconds_elapsed += 1
        if seconds_elapsed == 5:
            long_task.cancel()

    try:
        await long_task
    except CancelledError:
        print("Task cancelled")


async def main2():

    task = asyncio.create_task(delay(3))

    try:
        result = await asyncio.wait_for(task, 2)
    except TimeoutError:
        print("too long, we time out here")


async def main3():

    task = asyncio.create_task(delay(3))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), 2)

    except TimeoutError:
        print("This is taking too long, but you have shield")
        await task
        print("Now you see everything finishes because of shield")


if __name__ == "__main__":
    asyncio.run(main3())
