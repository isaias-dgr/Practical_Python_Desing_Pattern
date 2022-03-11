import time
from tracemalloc import start


def fib(n):
    if n < 2:
        return 1
    return fib(n-2)+fib(n-1)


if __name__ == "__main__":
    print(fib(4))

    # memoization
    start_time = time.time()
    fib_sequence = [fib(x) for x in range(1, 80)]
    end_time = time.time()
    print(f"""
        \rCalculating the list of {len(fib_sequence)}
        \rFibonacci number took {end_time - start_time} seconds
    """)
