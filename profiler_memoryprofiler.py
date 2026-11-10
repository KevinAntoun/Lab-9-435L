
import time
from memory_profiler import profile


@profile
def slow_function():
    time.sleep(2)
    n = 10000
    return n * (n - 1) * (2 * n - 1) // 6


@profile
def optimized_fast_function():
    n = 100
    return n * (n - 1) * (2 * n - 1) // 6


@profile
def memory_intensive_function():
    n = 10000000
    return n * (n - 1) * (2 * n - 1) // 6


def main():
    slow_function()
    optimized_fast_function()
    memory_intensive_function()


if __name__ == "__main__":
    main()
