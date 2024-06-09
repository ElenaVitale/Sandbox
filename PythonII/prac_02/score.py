
"""
Rewrite for Wk 2
CP1404/CP5632 - Practical
Broken program to determine score status

Main function - ask the use for their score and print result
Add a random number generator.
I really didn't understand what was meant to happen with the random score.
"""
import random

def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    if score > 90:
        print("Excellent")
    elif score > 49:
        print("Passable")
    else:
        print("Fail")

main()