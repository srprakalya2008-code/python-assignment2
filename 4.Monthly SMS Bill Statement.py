# Q4 - String Building Comparison

import time


def build_plus(parts):

    text = ""

    for p in parts:
        text += p + ","

    return text


def build_join(parts):

    return ",".join(parts) + ("," if parts else "")


def build_fstring(parts):

    result = []

    for p in parts:
        result.append(f"{p},")

    return "".join(result)


for size in [1000, 10000, 200000]:

    print("\nNumber of Lines:", size)

    items = [
        f"Item{i}:Rs{i % 50}"
        for i in range(size)
    ]

    # Plus method
    start = time.perf_counter()

    a = build_plus(items)

    t_plus = time.perf_counter() - start

    # Join method
    start = time.perf_counter()

    b = build_join(items)

    t_join = time.perf_counter() - start

    # F-string method
    start = time.perf_counter()

    c = build_fstring(items)

    t_fstring = time.perf_counter() - start

    print("Same Output:", a == b == c)

    print("String Length:", len(a))

    print("+ Time:", round(t_plus, 6), "seconds")

    print("Join Time:", round(t_join, 6), "seconds")

    print("F-string Time:", round(t_fstring, 6), "seconds")