"""
In the lecture there was a "do this now" activity similar to this,
so you can use what we did there to help with this program.

Write a complete Python program following the standard structure that uses a main and other functions.
Use a main menu following the standard menu pattern.

The menu should have four separate options:

    (G)et a valid score (must be 0-100 inclusive)
    (P)rint result (copy or import your function to determine the result from score.py)
    (S)how stars (this should print as many stars as the score)
    (Q)uit

Handle each of these (except quit) separately, and consider how you can reuse your functions.

In main(), before the menu loop, get a valid score using your function.
When the user quits, say some kind of "farewell".
"""

def main():
    menu = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""

    print(menu)
    choice = input("Select option from menu: ").upper()
    score = 0
    while choice != "Q":
        if choice == "G":
            # (G)et a valid score (must be 0-100 inclusive)
            score = get_score()

        elif choice == "P":
            # (P)rint result (copy or import your function to determine the result from score.py)
            print_result(score)

        elif choice == "S":
            # (S)how stars (this should print as many stars as the score)
            show_stars(score)

        else:
            print("Invalid option")
        print(menu)
        choice = input("Select option from menu: ").upper()
    print("Thank you, Farewell.")


def get_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

def print_result(score):
    if score > 90:
        print("Excellent")
    elif score > 49:
        print("Passable")
    else:
        print("Fail")

def show_stars(score):
    print("*" * score)

main()