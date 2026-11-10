
from line_profiler import LineProfiler

from profiler import (
    slow_function,
    optimized_fast_function,
    memory_intensive_function,
)


def main():
    profiler = LineProfiler()

    profiler.add_function(slow_function)
    profiler.add_function(optimized_fast_function)
    profiler.add_function(memory_intensive_function)

    profiler.enable_by_count()

    slow_function()
    optimized_fast_function()
    memory_intensive_function()

    profiler.disable_by_count()

    profiler.print_stats()


if __name__ == "__main__":
    main()
