import os
import time
import random
import multiprocessing as mp


S_CPU = int(os.getenv("S_CPU", 0))


def task(condition, event, number):
    os.sched_setaffinity(0, {S_CPU + 1 + number})

    while True:
        # wait to be notified
        print(f'Process {number} waiting...', flush=True)
        with condition:
            condition.wait()

        if not event.is_set():
            return

        # block for a moment
        value = random.random()

        # report a result
        print(f'Process {number} got {value}', flush=True)

        time.sleep(value)


if __name__ == '__main__':
    # create a condition
    event = mp.Event()
    event.set()
    condition = mp.Condition()

    # create all child processes
    processes = [mp.Process(target=task, args=(condition, event, i)) for i in range(3)]

    os.sched_setaffinity(0, {S_CPU})

    # start all child processes
    for process in processes:
        process.start()

    # block for a moment
    time.sleep(1)

    for i in range(32):
        print()
        print("iteration:", i, flush=True)
        print()

        # notify all waiting processes that they can run
        with condition:
            # wait to be notified
            condition.notify_all()

        # block for a moment
        time.sleep(1)

    # notify all workers
    event.clear()
    with condition:
        condition.notify_all()

    # wait for all child processes to terminate
    for process in processes:
        process.join()
