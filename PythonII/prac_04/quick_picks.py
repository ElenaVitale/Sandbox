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

number_of_picks = int(input("How many quick picks? "))

