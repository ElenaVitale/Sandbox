"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? If it's not a number
2. When will a ZeroDivisionError occur? When the denominator is zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, by not allowing a zero to be entered.

I've broken down the program into a number of elements with loops.
Used 'while True' loop to keep asking the user until they enter the correct information.
Try & Except for each user input.
Break exits the loop, couldn't get it to work with it.
Move the fraction calculation to inside the while try try loop.
"""
while True:

    try:
        numerator = int(input("Enter the numerator: "))
        break
    except ValueError:
        print("Numerator must be a valid number")

while True:

    try:
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        break
    except ValueError:
        print("Denominator must be a valid number.")
    except ZeroDivisionError:
        print("Zero denominator. Enter a valid digit")

print(fraction)
print("Finished.")


