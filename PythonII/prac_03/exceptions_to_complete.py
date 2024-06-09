"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task

Changed except to add ValueError so that it would work.
Added 'is_finished = True' to the point when value integer is entered
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print(f"Valid result is: {result}")


