import time


class ProfilingDecorator:

    def __init__(self, f):
        print("Profiling decorator initiaded")
        self.f = f

    def __call__(self, *args):
        print("ProfilingDecorator called")
        start_time = time.time()
        result = self.f(*args)
        end_time = time.time()
        print(f"[Time elapsed for n = {args}] {end_time-start_time}")
        return result


class toHTMLDecorator:

    def __init__(self, f):
        print("HTML wrapper initiated")
        self.f = f

    def __call__(self, *args):
        print("toHTMLDecorator called")
        return f"<html><body>{self.f(*args)}</body></html>"


@toHTMLDecorator
@ProfilingDecorator
def fib(n):
    print("Inside fib")
    if n < 2:
        return

    fibPrev = 1
    fib = 1

    for num in range(2, n):
        fibPrev, fib = fib, fib+fibPrev

    return fib


if __name__ == "__main__":
    n = 77
    print(f"Fibonacci number for n = {n}: {fib(n)}")
