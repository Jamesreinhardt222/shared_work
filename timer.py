import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"finished {func.__name__!r} in {run_time:4f} secs")
        return value
    return wrapper
