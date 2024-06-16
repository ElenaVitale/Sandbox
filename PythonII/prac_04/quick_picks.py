"""
Write a program that asks the user how many "quick picks" they wish to generate.
The program then generates that many lines of output.
Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS.
Each line (quick pick) should not contain any repeated number.
Each line of numbers should be displayed in sorted (ascending) order.
Study the formatting below so that numbers align neatly.
Python's random module has a sample() function, which returns a selection from a list.
This is a nice way to solve this problem... but it's too easy :)
Do not use it for this program.
Your code should produce output that matches this sample output
(except the numbers are random):
"""

import random

#Constants
NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def generate_quick_pick():
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick

def main():
    number_of_picks = int(input("How many quick picks? "))
    for number in range (number_of_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))

main()

