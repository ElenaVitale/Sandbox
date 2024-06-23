"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# if/else loop breaks pretty quickly - will need to fix

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {
    "QLD":"Queensland",
    "NSW": "New South Wales",
    "NT" : "Northern Territory",
    "WA" : "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

max_code_length = max(len(code) for code in CODE_TO_NAME)

for code, name in CODE_TO_NAME.items():
    print(f"{code:<{max_code_length}} is {name}")


state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")