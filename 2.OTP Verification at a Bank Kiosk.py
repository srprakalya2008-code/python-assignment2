# Q2 - OTP Verification Using Loops

CORRECT_OTP = "123456"


def verify_while():

    attempts = 0

    while attempts < 3:

        otp = input("Enter OTP: ").strip()

        if otp == "":
            print("Blank entry. Try again.")
            continue

        attempts += 1

        if otp == CORRECT_OTP:
            print("OTP Verified Successfully!")
            break

        print("Incorrect OTP!")

    else:
        print("Account locked for 30 minutes.")


def verify_for():

    for attempt in range(3):

        otp = input("Enter OTP: ").strip()

        if otp == "":
            print("Blank entry. Try again.")
            continue

        if otp == CORRECT_OTP:
            print("OTP Verified Successfully!")
            break

        print("Incorrect OTP!")

    else:
        print("Account locked for 30 minutes.")


print("1. While Loop")
print("2. For Loop")

choice = input("Choose Option: ").strip()

if choice == "1":
    print("\nUsing While Loop")
    verify_while()

elif choice == "2":
    print("\nUsing For Loop")
    verify_for()

else:
    print("Invalid Choice! Enter 1 or 2.")