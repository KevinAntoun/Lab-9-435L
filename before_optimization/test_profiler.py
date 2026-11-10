
import time
import unittest
import memory_profiler

from profiler import (
    slow_function,
    fast_function,
    memory_intensive_function
)


class TestProfiler(unittest.TestCase):

    def time_function(self, func):
        """Measure the execution time of a function."""
        start_time = time.perf_counter()

        func()

        end_time = time.perf_counter()

        return end_time - start_time

    def test_slow_function(self):
        """Test the slow_function for execution time."""
        duration = self.time_function(slow_function)

        print(f"slow_function executed in {duration:.2f} seconds.")

        self.assertGreaterEqual(
            duration, 1.9,
            "slow_function should take approximately 2 seconds."
        )

    def test_fast_function(self):
        """Test the fast_function for execution time."""
        duration = self.time_function(fast_function)

        print(f"fast_function executed in {duration:.2f} seconds.")

        self.assertLess(
            duration, 1,
            "fast_function should take less than 1 second."
        )

    def test_memory_intensive_function(self):
        """Test execution time and peak memory usage."""

        start_time = time.perf_counter()

        mem_usage = memory_profiler.memory_usage(
            (memory_intensive_function, (), {}),
            interval=0.01,
            max_usage=False,
            include_children=True
        )

        duration = time.perf_counter() - start_time

        baseline_memory = mem_usage[0]
        peak_memory = max(mem_usage)

        print(
            f"memory_intensive_function executed in "
            f"{duration:.2f} seconds."
        )

        print(
            f"Baseline memory: {baseline_memory:.2f} MiB"
        )

        print(
            f"Peak memory: {peak_memory:.2f} MiB"
        )

        self.assertLess(
            duration, 5,
            "memory_intensive_function should take less than 5 seconds."
        )

        self.assertGreater(
            peak_memory,
            baseline_memory,
            "Memory usage should increase during execution."
        )


def main():
    unittest.main()


if __name__ == "__main__":
    main()
