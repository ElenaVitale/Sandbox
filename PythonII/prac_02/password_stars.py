"""
Print stars for password.
write a program that asks the user for a password,
with error-checking to repeat if the password doesn't meet a minimum length set by a variable.


"""

# Print stars for password
minimum_length = 5
def print_stars():

    password = input("Enter a password: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input("Enter a password: ")
    print("*" * len(password))

print_stars()
