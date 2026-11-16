# Q3 - Vehicle Registration Validator

def normalise(reg):

    reg = reg.strip().upper()

    reg = reg.replace(" ", "")
    reg = reg.replace("-", "")

    return reg


def is_valid(reg):

    if len(reg) not in (9, 10):
        return False

    if not reg[0:2].isalpha():
        return False

    if not reg[2:4].isdigit():
        return False

    if not reg[4:-4].isalpha():
        return False

    if len(reg[4:-4]) not in (1, 2):
        return False

    if not reg[-4:].isdigit():
        return False

    return True


def format_receipt(reg):

    if not is_valid(reg):
        return "INVALID"

    return reg[:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]


registrations = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN09AB1234",
    "TN 22 1234 AB",
    "MH 12 XYZ 4567",
    "TN-09-A-1234"
]

for raw in registrations:

    reg = normalise(raw)

    if is_valid(reg):
        print(raw, "->", reg, "VALID")
        print("Receipt:", format_receipt(reg))

    else:
        print(raw, "->", reg, "INVALID")