import time


class Calculator:

    def fib_cache(self, n, cache):
        if n < 2:
            return 1

        if n in cache:
            return cache[n]

        cache[n] = self.fib_cache(n-2, cache) + self.fib_cache(n-1, cache)
        return cache[n]


if __name__ == "__main__":
    cache = {}
    start_time = time.time()
    c = Calculator()
    fib_sequence = [c.fib_cache(x, cache) for x in range(0, 80)]
    end_time = time.time()
    print(f"""
        \rCalculating the list of {len(fib_sequence)} {fib_sequence[-1]}
        \rFibonacci number took {end_time - start_time} seconds
    """)
