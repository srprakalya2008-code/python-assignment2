# Q6 - Recursion and Its Limits
# No external modules required

# Count function calls
naive_calls = 0
memo_calls = 0


# 1. Naive Recursion
def ways_naive(n):
    global naive_calls

    naive_calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


# 2. Memoisation using Dictionary
def ways_memo(n, cache=None):
    global memo_calls

    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]

    memo_calls += 1

    if n <= 1:
        return 1

    cache[n] = (
        ways_memo(n - 1, cache) +
        ways_memo(n - 2, cache)
    )

    return cache[n]


# 3. Iterative Dynamic Programming
def ways_iterative(n):

    if n <= 1:
        return 1

    a = 1
    b = 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


# Hand Calculation Verification
print("HAND CALCULATION VERIFICATION")

for n in range(1, 7):
    print("Steps:", n,
          "Ways:", ways_iterative(n))


# Naive Recursion vs Memoisation
print("\nNAIVE RECURSION VS MEMOISATION")

for n in [10, 20, 25, 30]:

    naive_calls = 0
    memo_calls = 0

    result1 = ways_naive(n)

    result2 = ways_memo(n)

    print("\nNumber of Steps:", n)

    print("Naive Result:", result1)
    print("Naive Function Calls:", naive_calls)

    print("Memoised Result:", result2)
    print("Memoised Function Calls:", memo_calls)


# Test Memoisation for 1000 Steps
print("\nMEMOISATION FOR 1000 STEPS")

memo_calls = 0

try:
    result = ways_memo(1000)

    print("Number of Ways:", result)

    print("Function Calls:", memo_calls)

except RecursionError:
    print("Recursion limit reached!")


# Iterative Method for 1000 Steps
print("\nITERATIVE METHOD FOR 1000 STEPS")

result = ways_iterative(1000)

print("Number of Ways:", result)

print("Iterative method executed successfully!")