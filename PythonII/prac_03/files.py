"""
Do from scratch exercises
Write python file that contains a number of different programs
1. Write code that asks the user for their name, then opens a file called
name.txt and writes that name to it. Use open and close for this question.
2. In the same file, but as if it were a separate program, write code that
opens "name.txt" and reads the name (as above) then prints (note the exact output),
Hi Bob! (or whatever the name is in the file). Do not simply print the user's input variable!
Use open and close for this question.
3. Create a text file called numbers.txt and save it in your prac directory.
Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens numbers.txt, reads only the first two numbers, adds them together
then prints the result, which should be... 59. Use with instead of open and close
for this question.
4. Now write a fourth block of code that prints the total for all lines in numbers.txt. This should work for a file with
any number of numbers. Use with instead of open and close for this question.
"""

def write_user_name_to_file():
    name = input("Enter your name: ")
    out_file = open("name.txt", "w")
    print(name, file=out_file)
    print("Finished.")
    out_file.close()

write_user_name_to_file()

def read_user_name_greet():
    file = open("name.txt", "r")
    name = file.read().strip()
    file.close()
    print(f"Hi {name}!")
    print("Completed.")

read_user_name_greet()

def calculate_sum():
    with open("numbers.txt", "r") as file:
        num1 = int(file.readline().strip())
        num2 = int(file.readline().strip())
        print(num1 + num2)

calculate_sum()

def sum_total_numbers():
    total = 0
    with open("numbers.txt", "r") as file:
        for line in file:
            total += int(line.strip())
    print(total)

sum_total_numbers()