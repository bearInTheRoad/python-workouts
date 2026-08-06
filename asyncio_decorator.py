import functools
import time
import asyncio
from typing import Callable


def async_timer(wait_seconds):
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            start = time.time()
            result = await func(*args, **kwargs)
            time.sleep(wait_seconds)
            end = time.time()
            print(end - start)
            return result

        return wrapped

    return wrapper


@async_timer(0)
async def delay(seconds):
    await asyncio.sleep(seconds)


@async_timer(0)
async def main():
    delay1 = asyncio.create_task(delay(3))
    delay2 = asyncio.create_task(delay(5))

    await delay1
    await delay2


if __name__ == "__main__":
    asyncio.run(main())
