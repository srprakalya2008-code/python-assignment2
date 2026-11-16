# Q7 - Diagnose, Redesign and Validate

import time
from functools import lru_cache


# Original recursive solution
@lru_cache(maxsize=None)
def original_program(n):

    if n <= 1:
        return 1

    return original_program(n - 1) + original_program(n - 2)


# Redesigned iterative solution
def redesigned_program(n):

    if n <= 1:
        return 1

    previous = 1
    current = 1

    for i in range(2, n + 1):

        previous, current = current, previous + current

    return current


# Validation
print("PROGRAM VALIDATION")

for n in [5, 10, 20, 100, 500, 1000]:

    original_program.cache_clear()

    start = time.perf_counter()

    try:

        old_result = original_program(n)

        old_time = time.perf_counter() - start

    except RecursionError:

        old_result = None

        old_time = None

    start = time.perf_counter()

    new_result = redesigned_program(n)

    new_time = time.perf_counter() - start

    print("\nInput:", n)

    print("Original Result:", old_result)

    print("Redesigned Result:", new_result)

    print("Same Result:", old_result == new_result)

    print("Original Time:", old_time)

    print("Redesigned Time:", new_time)


print("\nREDESIGN ANALYSIS")

print("Original approach: Memoised recursion")

print("Redesigned approach: Iterative dynamic programming")

print("Time Complexity: O(n)")

print("Space Complexity: O(1)")