import time


def timer(func):
    """Print the runtime of the decorated function"""

    def wrapper(*args, **kwargs):
        """
        Decorator function for finding the amount of time it takes to complete a function.

        Will append the time it takes to complete the function to a text file called "results.txt."
        :return: returns whatever gets returned from the function being decorated.
        """
        start_time = time.perf_counter_ns()
        value = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        run_time = end_time - start_time
        filename = "results.txt"
        with open(filename, 'a') as file_object:
            print(args[0])
            file_object.write(f"Finished {func.__name__!r} for !{args[0]} in {run_time:.4f} nanosecs\n")
        return value

    return wrapper


@timer
def factorial_iterative(number):
    """
    Use a while loop to find the factorial for a number.

    :param number: an int.
    :precondition number: must be an int greater than zero.
    :postcondition: will return the factorial of the number.
    :return: an int.

    >>>>
    """
    factorial = 1
    while True:
        if number == 1:
            break
        factorial *= number
        number -= 1
    return factorial


def factorial_recursive_helper(number):
    """
    Preforms the calculation to get the factorial of a number

    :param number: an Int.
    :precondition number: must be an int greater than zero.
    :return: an int
    """
    if number == 1:
        return 1
    else:
        return number * factorial_recursive_helper(number - 1)


@timer
def factorial_recursive(number):
    """
    Calls a helper function to use the recursive calculation.

    This function can be decorated with the timer function to find the amount of time it takes for
    its helper function to recursively calculate a factorial for the argument, "number."
    :param number: an int.
    :precondition number: must be an int greater than zero.
    :postcondition, the helper function will return the final answer to this function.
    :return: an int.
    """
    return factorial_recursive_helper(number)


def main():
    for number in range(1, 101):
        factorial_iterative(number)
        factorial_recursive(number)


if __name__ == "__main__":
    main()
