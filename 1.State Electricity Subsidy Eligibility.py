# Q1 - Electricity Subsidy Eligibility

def separate_if(units, ration_card, age):
    result = []

    if units <= 100:
        result.append("Full Subsidy")

    if 101 <= units <= 200 and ration_card:
        result.append("Partial Subsidy")

    if units > 200 and age > 80:
        result.append("Special Subsidy")

    if not result:
        result.append("No Subsidy")

    return result


def chained_if(units, ration_card, age):

    if units <= 100:
        return "Full Subsidy"

    elif 101 <= units <= 200 and ration_card:
        return "Partial Subsidy"

    elif units > 200 and age > 80:
        return "Special Subsidy"

    else:
        return "No Subsidy"


households = [
    (100, False, 30),
    (101, True, 40),
    (101, False, 50),
    (200, True, 65),
    (200, False, 81),
    (201, False, 85),
    (201, True, 60),
    (80, True, 82)
]

print("Electricity Subsidy Results")

for units, ration, age in households:

    print("\nUnits:", units)
    print("Ration Card:", ration)
    print("Age:", age)

    print("Separate If:", separate_if(units, ration, age))

    print("If-Elif-Else:",
          chained_if(units, ration, age))