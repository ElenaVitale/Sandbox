"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_data(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_list = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data_list.append(parts)
    input_file.close()
    return data_list


def display_data(data):
    """Display the loaded and formatted data"""
    for subject, lecturer, number_of_students in data:
        print(f"{subject} is taught by {lecturer} and has {number_of_students} students.")


main()
