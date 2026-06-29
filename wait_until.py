import time


def wait_until(iterable, min_seconds):
    """
    wait until min_seconds before you can yield
    the next value in iterable
    """
    t0 = 0

    for value in iterable:
        t1 = time.perf_counter()
        if t1 - t0 < min_seconds:
            print(f"you need to wait {min_seconds - (t1 - t0)} seconds")
            time.sleep(min_seconds - (t1 - t0))
        t1 = time.perf_counter()
        yield value
        t0 = t1


min_seconds = 3
iterable = range(10)
for value in wait_until(iterable, min_seconds):
    print(value)
