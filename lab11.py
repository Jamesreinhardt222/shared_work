import time


def timer(func):
    """Print the runtime of the decorated function"""

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        filename = "results.txt"
        with open(filename, 'a') as file_object:
            file_object.write(f"Finished {func.__name__!r} in {run_time:.4f} secs\n")
        return value

    return wrapper


@timer
def factorial_iterative(n):
    factorial = 1
    while True:
        if n == 1:
            break
        factorial *= n
        n -= 1
    return factorial


def factorial_recursive_helper(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive_helper(n - 1)


@timer
def factorial_recursive(n):
    return factorial_recursive_helper(n)


def main():
    for n in range(1, 101):
        factorial_iterative(n)
        factorial_recursive(n)
        # print(f"factorial_iterative({n}) : {factorial_iterative(n)}\n")
        # print(f"factorial_recursive({n}) : {factorial_recursive(n)}\n")


if __name__ == "__main__":
    main()
