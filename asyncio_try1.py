"""Asyncio sandbox: one thread, one event loop, many coroutines.

Mental model
------------
- asyncio is cooperative concurrency on a *single* thread, not OS threads.
- Only one coroutine runs at a time. Others are either queued (ready) or
  parked waiting on I/O / timers / other tasks.
- `async def` defines a coroutine function. Calling it builds a coroutine
  object; nothing runs until the event loop drives it.
- `await X` means: suspend *this* coroutine until *this specific* X is done,
  hand control back to the event loop, then resume here with X's result.
  It is NOT "pop the first finished thing from a shared results queue."
- `asyncio.create_task(coro)` wraps coro in a Task and *schedules* it on the
  loop's ready queue. It does NOT jump into coro immediately — the caller
  keeps running until it awaits or returns. The task actually starts only
  when the loop next gets control (some running coroutine awaits/finishes).
- Overlap happens while tasks are parked on waits (e.g. asyncio.sleep).
  Wall-clock time for N concurrent sleeps ≈ max(durations), not sum.
- If main finishes and asyncio.run() tears the loop down, pending tasks are
  cancelled. You lose the return value, may lose exceptions ("Task exception
  was never retrieved"), and the work may never complete — not merely a
  "swallowed return."

Switch the asyncio.run(...) call at the bottom to compare mains.
"""

import asyncio


async def delay(seconds):
    """Stand-in for any awaitable I/O-bound unit of work.

    Prints bracketing the sleep make scheduling visible: 'start' runs when
    the task first gets the loop; 'finished' runs only if the sleep is
    allowed to complete (not cancelled at shutdown).
    """
    print(f"start sleeping for {seconds} seconds")
    await asyncio.sleep(seconds)
    print(f"finished sleeping for {seconds} seconds")

    return seconds


async def main1():
    """Sequential awaits: no overlap. Wall clock ≈ 3 + 5 = 8s.

    `await delay(3)` runs that coroutine to completion before the next line.
    The second delay does not even start until the first is fully done —
    contrast with create_task + concurrent awaits in main3/main5.
    """
    await delay(3)
    a = 1 + 3
    print(f"this is the value of {a}")

    await delay(5)


async def main2():
    """create_task schedules work; await is how *this* coroutine waits for it.

    create_task queues delay(3) but does not run it yet. The following
    `await sleep_for_three` yields to the loop, which then starts the task,
    lets it sleep, and only resumes main2 when that *specific* task finishes.
    Wall clock ≈ 3s. result is the task's return value (seconds).
    """
    sleep_for_three = asyncio.create_task(delay(3))

    result = await sleep_for_three
    a = 1 + 3
    print(f"this is the value of {a}")
    print(result)


async def main3():
    """Two tasks scheduled up front; sleeps overlap. Wall clock ≈ max(3, 5) = 5s.

    Both create_task calls only queue work. main3 keeps running until the
    first await, then the loop starts the ready tasks one-at-a-time until
    each hits its own await sleep — after that both are sleeping concurrently.

    await sleep_for_three parks main3 until the 3s task done (~3s in).
    By then the 5s task has ~2s left, so await sleep_for_five only waits the
    remainder. Code after both awaits runs only once *both* have finished.
    Total is NOT 3+5 because the waits overlapped.
    """
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_for_five = asyncio.create_task(delay(5))

    await sleep_for_three
    await sleep_for_five
    a = 1 + 3
    print(f"this is the value of {a}")


async def main4():
    """Fire-and-forget pitfall: schedule without ever yielding long enough.

    create_task only queues delay(3). main4 then prints and returns immediately,
    so the task typically has not even started while main4 was running.

    Actual order is roughly:
      1) main4 schedules the task (still not running)
      2) main4 prints "done" and returns
      3) loop may briefly start delay during teardown ("start sleeping...")
      4) asyncio.run() cancels pending tasks — usually no "finished sleeping"
         and no usable return value

    So: task is scheduled, not "already running to completion." Exiting main
    is cancellation + lost result/errors, not just a swallowed return.
    """
    sleep_for_three = asyncio.create_task(delay(3))
    print("done")


async def hello_every_second():
    """Small coroutine whose awaits *are* the windows other tasks run in.

    Each await asyncio.sleep(1) yields to the loop. That is when queued work
    from the caller (e.g. main5's delay tasks) gets to start or progress.
    Without these awaits, sibling tasks would stay stuck in the ready queue.
    """
    for i in range(3):
        print(f"hello {i}")
        await asyncio.sleep(1)


async def main5():
    """Background tasks progress during another coroutine's awaits. ~3s total.

    Timeline (cooperative, single-threaded — "same time" means overlapping waits):
      t≈0  create_task x2 → both delays QUEUED only, neither has printed yet
      t≈0  await hello_every_second() starts hello (not the delays first)
      t≈0  hello prints "hello 0", then await sleep(1) → yields to loop
      t≈0  loop runs ready tasks roughly FIFO: first_delay, then second_delay.
           Each prints "start sleeping..." and parks on sleep(3). Startup is
           back-to-back on one thread, not true parallel CPU; only the sleeps overlap.
      t≈1  hello resumes → "hello 1" → sleep again (delays still sleeping)
      t≈2  hello → "hello 2" → sleep again
      t≈3  hello finishes; delays are also ~done
      t≈3  await first_delay / await second_delay: if already finished, return
           immediately; if not, wait out whatever remains. We do NOT skip them
           or "prefer hello regardless of delay status" after hello ends —
           hello is simply over, and the next awaits gate on the delay tasks.

    Who runs first among ready tasks? Usually FIFO (first scheduled first),
    but that is a scheduler detail — don't build correctness on exact order.
    Concurrent here means interleaved on one thread whenever something awaits.
    """
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))

    await hello_every_second()

    await first_delay
    await second_delay


if __name__ == "__main__":
    asyncio.run(main5())
