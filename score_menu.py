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

menu = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""

choice = input("Select option from menu: ").upper()
while choice != "Q":
    if choice == "G":
        # (G)et a valid score (must be 0-100 inclusive)

        pass

    elif choice == "F":
        # (P)rint result (copy or import your function to determine the result from score.py)
        pass

    elif choice == "S":
        # (S)how stars (this should print as many stars as the score)
        pass

    else:
        print("Invalid option")
        print(menu)
        choice = input("Select option from menu: ").upper()
print("Thank you, Farewell.")
# display menu
# get choice
# while choice != <quit option>
#     if choice == <first option>
#         <do first task>
#     else if choice == <second option>
#         <do second task>
#     ...
#     else if choice == <n-th option>
#         <do n-th task>
#     else
#         display invalid input error message
#     display menu
#     get choice
# <do final thing, if needed>