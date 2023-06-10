"""
Write a program that asks the user for a password, with error-checking
to repeat if the password doesn't meet a minimum length set by variable.
The program should then print asterisks as long as the word.
Example: if the user enters Pythonista (10 characters), the program
should print **********.
"""
# Lindsay - my understanding/interpretation of this question is...
"""
- Ask for password from user
- Use error checking (from programming patterns) to compare length of 
password with the minimum length set by the variable
- The minimum length is set by a variable, but the user doesn't input/contribute 
to setting the minimum length variable.
- password < minimum length - error message and enter again
- If password length is correct, => variable minimum length, print number of *
equal to the length of the password.
"""
# Since I only got 2/4 on last week's prac, I thought I'd detail my thought process
# this way we can see where I'm going wrong & correct it.
"""
I've done this in microsteps, and had to add/delete as I problem solved.
After writing it out a few times, I built it slowly in earnest.
I started with a basic 'enter number' then printed the number
I build the for loop (that I don't use in the end) to make sure I 
remembered how to print stars. 
Built the while loop checking with just a number. Once this worked I removed
the int to make it a string value
Looked up how exactly to use the 'len' function. Tried to make it work in
the while loop and it worked. Happy dance. 

PS. I keep this for loop for my reference & revision later.
#program to enter number, then print number of stars.
num_stars = int(input("Enter number: "))
for i in range(0,num_stars):
    print("*", end=" ")
print()
"""


#print the password length in stars.
password = (input("Enter password: "))
minimum_password_length = 6
while len(password) < minimum_password_length:
    print(f"password must be {minimum_password_length} characters or greater")
    password = (input("Enter password: "))
print(len(password) * "*")


