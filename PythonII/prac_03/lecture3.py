"""
L1 try, except
"""

"""
L2 - open and close files. Write and read to files. 
strip.      line.strip()
read files
in_file.read(n)
in_file.readline()
in_file.readlines()

"""

"""
Slide 19. 
Do the whole of one job in a reusable way (SRP)
Good Design

"""

# def main():
#     filename = "file.txt"
#     process(filename)
#
# def process(filename):
#     out_file = open(filename, 'w')
#     for i in range(99):
#         print("problem", file=file_object)
#         out_file.close()


# Slide 8
# FILENAME = "testfile.txt"
# in_file = open(FILENAME)
# text = in_file.read()
# in_file.close()
# print(text)

# s = "\tPython, Monty   \n"
# print(s[1], ".", sep="")
# print(s.strip(), ".", sep="")
# s = s.replace(' ', '*') #original didn't change the s (variable)
# print(s.lstrip(), ".", sep="")
# print(s.strip().split(','))

# writes the name to a file
# name = input("Name: ")
# out_file = open("name.txt", "w")
# print(name, file=out_file)
# out_file.close()

# Exercise from seminar
# names = ['Bennie', 'Jazz', 'Cindy']
# out_file = open("name.txt", "w")
# for name in names:
#     out_file.write(name + " ")
#     print(name)
# print("Completed")

# valid_input = False
# while not valid_input:
#     try:
#         age = int(input("Age: "))
#         valid_input = True
#     except ValueError:
#         print("Invalid (not an integer)")
# print("Next year you will be", age + 1)

#Convert a string to an integer
# def convert_str_to_int(text):
#     """ LBYL version"""
#     if not isinstance(text, str) or not text.isdigit():
#         return None
#     else:
#         return int(text)
#
# def convert_str_to_int(text):
#     """EAFP version"""
#     try:
#         return int(text)
#     except ValueError:
#         return None