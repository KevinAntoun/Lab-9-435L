
import time
import unittest
import memory_profiler

from profiler import (
    slow_function,
    optimized_fast_function,
    memory_intensive_function,
)


class TestProfiler(unittest.TestCase):

    def time_function(self, func):
        """Times the execution of a function."""
        start_time = time.perf_counter()
        result = func()
        end_time = time.perf_counter()
        return end_time - start_time, result

    def test_slow_function(self):
        """Test slow_function execution time."""
        duration, result = self.time_function(slow_function)

        print(f"slow_function executed in {duration:.2f} seconds.")

        self.assertGreaterEqual(duration, 2)
        self.assertEqual(
            result, 9999 * 10000 * 19999 // 6
        )

    def test_optimized_fast_function(self):
        """Test the optimized function."""
        duration, result = self.time_function(
            optimized_fast_function
        )

        print(
            f"optimized_fast_function executed in "
            f"{duration:.6f} seconds."
        )

        self.assertLess(duration, 1)
        self.assertEqual(result, 328350)

    def test_memory_intensive_function(self):
        """Test calculation and monitor memory usage."""
        mem_usage_before = memory_profiler.memory_usage()

        duration, result = self.time_function(
            memory_intensive_function
        )

        mem_usage_after = memory_profiler.memory_usage()

        print(
            f"memory_intensive_function executed in "
            f"{duration:.2f} seconds."
        )

        print(
            f"Memory usage before: "
            f"{mem_usage_before[0]:.2f} MiB, "
            f"after: {mem_usage_after[0]:.2f} MiB."
        )

        n = 10000000
        expected = n * (n - 1) * (2 * n - 1) // 6

        self.assertEqual(result, expected)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
