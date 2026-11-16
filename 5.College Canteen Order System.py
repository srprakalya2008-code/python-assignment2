# Q5 - Functions, Parameters and Scope


# Buggy function
def add_item_buggy(item, order=[]):

    order.append(item)

    return order


# Correct function
def add_item(item, order=None):

    if order is None:
        order = []

    order.append(item)

    return order


# Positional and keyword arguments
def calculate_bill(amount, gst_rate=0.05):

    gst = amount * gst_rate

    total = amount + gst

    return total, gst


# Global variable
count = 0


def global_example():

    global count

    count += 1

    return count


# Nonlocal variable
def counter_function():

    value = 0

    def increment():

        nonlocal value

        value += 1

        return value

    return increment


print("BUGGY FUNCTION")

print(
    add_item_buggy("Tea"),
    add_item_buggy("Vada")
)

print("Default Values:", add_item_buggy.__defaults__)


print("\nCORRECT FUNCTION")

print(
    add_item("Tea"),
    add_item("Vada")
)


print("\nThree Customer Orders")

order1 = add_item("Idli")
order2 = add_item("Dosa")
order3 = add_item("Pongal")

print("Customer 1:", order1)
print("Customer 2:", order2)
print("Customer 3:", order3)


print("\nBILL CALCULATION")

total, gst = calculate_bill(200, gst_rate=0.05)

print("GST:", gst)
print("Total:", total)


print("\nGLOBAL VARIABLE")

print(global_example())
print(global_example())


print("\nNONLOCAL VARIABLE")

counter = counter_function()

print(counter())
print(counter())
print(counter())