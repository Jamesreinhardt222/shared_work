import time


def timer(func):
    """Print the runtime of the decorated function"""

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
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

@timer
def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        factorial = 1
        factorial *= n
        return factorial_iterative(n)


def main():
    print(factorial_iterative(1))
    print(factorial_iterative(2))
    print(factorial_iterative(3))
    print(factorial_iterative(4))
    print(factorial_iterative(5))
    print(factorial_iterative(6))
    #print(factorial_recursive(1))
    #print(factorial_recursive(2))
    #print(factorial_recursive(3))
    #print(factorial_recursive(4))
    print(factorial_recursive(5))
    print(factorial_recursive(6))


if __name__ == "__main__":
    main()