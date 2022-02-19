import time
from unittest import result


def fib(n):
    start_time = time.time()
    if n < 2:
        return

    fibPrev = 1
    fib = 1

    for num in range(2, n):
        fibPrev, fib = fib, fib+fibPrev

    end_time = time.time()

    print(f"[Time elapsed for n = {n} ] {end_time-start_time}")
    return fib


if __name__ == "__main__":
    n = 77
    print(f"Fibonacci number for n = {n}: {fib(n)}")
