import time


def timer(func):
    """Print the runtime of the decorated function"""

    def wrapper(*args, **kwargs):
        filename = "results.txt"
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        
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
        return factorial_recursive_helper(n - 1)


def factorial_recursive_helper(n):
    answer = 1
    for number in range (1, n):
        answer*= number
    return answer


def main():
    for n in range(1, 101):
        print(f"factorial_iterative({n}) : {factorial_iterative(n)}\n")
        print(f"factorial_recursive({n}) : {factorial_recursive(factorial_recursive_helper(n))}\n")


if __name__ == "__main__":
    main()
