"""
Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
The program should then output information about these numbers, as in the output below.
You can use the functions min, max, sum and len, and you can use the append method to add a number

*** # Notes and has
"""


def main():
    get_numbers()
    display_numbers()

def get_numbers():
    global numbers
    numbers = []
    for count in range(5):
        number = int(input(f"Enter number {count + 1}: "))
        numbers.append(number)

def display_numbers():
    print(f"The first number is: {numbers[0]} ")
    print(f"The last number is: {numbers[-1]} ")
    print(f"The smallest number is: {min(numbers)}")
    print(f"The largest number is: {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

main()