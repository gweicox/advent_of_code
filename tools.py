from functools import wraps
from time import perf_counter


def timer(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = perf_counter()
        value = func(*args, **kwargs)
        tac = perf_counter()
        elapsed_time = f"[{(tac - tic):0.4f} sec]"
        return value, elapsed_time
    return wrapper_timer
