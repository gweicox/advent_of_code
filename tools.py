from functools import wraps
from time import perf_counter


def timer(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = perf_counter()
        ans = func(*args, **kwargs)
        tac = perf_counter()
        elapsed_time = tac - tic
        print(f"{ans} [{elapsed_time:0.4f} sec]")
        return ans
    return wrapper_timer
