import time
import random


def elpased_since(iterable):
    t0 = None

    for value in iterable:
        t1 = time.perf_counter()
        yield int(t1 - (t0 or t1)), value
        t0 = t1


iterable = range(10)
for interval, value in elpased_since(iterable):
    # for each value in iterable, it will give both the value
    # and the number of seconds since last sleep
    print(interval, value)
    sleep_time = random.randint(1, 3)
    print(f"we will sleep for {sleep_time} seconds")
    time.sleep(sleep_time)
