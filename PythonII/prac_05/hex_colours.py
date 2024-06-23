"""Based on the state name example program above, create a program that allows you
to look up hexadecimal colour codes like those at http://www.color-hex.com/color-names.html

Use a constant dictionary of about 10 colour names and write a program that allows a user
to enter a name and get the code, e.g., entering AliceBlue (or aliceblue - make it case-independent)
should show #f0f8ff.

Entering an invalid colour name should not crash the program.
Allow the user to enter names until they enter a blank one to stop the loop.

Note: We have just done two exercises that use dictionaries that are constants and named in ALL_CAPS.
Please don't think this is any kind of rule or pattern.
Dictionaries that change would not be constants."""

COLOUR_CODES = {
    'aliceblue': 'f0f8ff',
    'amaranth': 'e52b50',
    'amber': 'ffbf00',
    'amethyst': '9966cc',
    'antiquewhite': 'faebd7',
    'apricot': 'fbceb1',
    'aqua': '00ffff',
    'asparagus': '87a96b',
    'beaver': '9f8170',
    'black': '000000',
}

def print_colour_names():
    for name in COLOUR_CODES:
        print(name.lower())

def get_hex_code(colour_name):
    return COLOUR_CODES.get(colour_name.lower())

def get_colour_name():
    colour_name = input("Enter colour name to get hex code: ").lower().strip()
    while colour_name != "":
        hex_code = get_hex_code(colour_name)
        if hex_code:
            print(f"The hexadecimal code for {colour_name} is #{hex_code}.")
        colour_name = input("Enter colour name to get hex code: ").lower().strip()
    print("Finished. Goodbye")

def main():
    print("Here is a list of colour names.")
    print_colour_names()
    get_colour_name()


main()
