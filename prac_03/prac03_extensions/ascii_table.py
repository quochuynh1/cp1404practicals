"""Program to convert from string to ASCII and vice versa"""

LOWER = 33
UPPER = 127



def main():
    is_valid_character = False
    character = input("Enter a character: ")
    # character = "a"
    while not is_valid_character:
        try:
            ascii_conversion = convert_character_to_ascii(character)
            print(f"'ASCII code for '{character}' is: {ascii_conversion}")
            is_valid_character = True
        except TypeError:
            print("Must be a valid character")
            character = input("Enter a character: ")

    is_valid_number = False
    while not is_valid_number:
        try:
            number = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
            integer_conversion = convert_integer_to_character(number)
            print(f"The character for '{number}' is '{integer_conversion}'")
            is_valid_number = True
        except TypeError:
            print("Must be between 33 and 127")
        except ValueError:
            print("Must be an integer")


def convert_character_to_ascii(character):
    ascii_value = ord(character)
    return ascii_value


def convert_integer_to_character(number):
    if number < LOWER or number > UPPER:
        raise TypeError("Number out of range")
    else:
        integer_as_character = chr(number)
        return integer_as_character


main()
