
import time

from functools import wraps


def profiling_wrapper(unit):

    def profiling_decorator(f):

        @wraps(f)
        def wrap_f(*args, **kwargs):
            start_time = time.time()
            result = f(*args, **kwargs)
            end_time = time.time()

            elapsed_time = end_time-start_time
            print(f"[Time elapsed for n  = {args}] {elapsed_time} {unit}")
            return result

        return wrap_f

    return profiling_decorator


# Dont work studi class decorator
def profile_all_class_methods(Cls):

    class ProfiledClass:

        def __init__(self, *args, **kwargs):
            self.inst = Cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                x = super(ProfiledClass, self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                x = self.inst.__getattribute__(s)
                if type(x) == type(self.__init__):
                    return profiling_wrapper(x)
                else:
                    return x

    return ProfiledClass


@profile_all_class_methods("miliseconds")
class DoMathStuff:

    def fib(self, n):
        print("Inside fib")
        if n < 2:
            return

        fibPrev = 1
        fib = 1

        for num in range(2, n):
            fibPrev, fib = fib, fibPrev

        return fib

    def factorial(self):
        print("Do the factorial")


if __name__ == "__main__":
    n = 77
    math = DoMathStuff()
    print(f"Fibonacci number for n = {n}: {math.fib(n)}")
