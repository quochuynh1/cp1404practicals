"""Program to convert from string to ASCII and vice versa"""

import random

def main():
    is_valid_character = False
    # character = input("Enter a character: ")
    character = "a"
    while not is_valid_character:
        try:
            ascii_conversion = convert_character_to_ascii(character)
            print(f"'ASCII code for '{character}' is: {ascii_conversion}")
            is_valid_character = True
        except TypeError:
            print("Must be a valid character")
            character = input("Enter a character: ")

    number = int(input("Enter a number between 33 and 127: "))
    # number = random.randint(33, 127)
    while number < 33 or number > 127:
        print("Invalid input")
        number = int(input("Enter a number between 33 and 127: "))
    try:
        integer_conversion = convert_integer_to_character(number)
        print(f"The character of '{number}' is '{integer_conversion}'")
    # except TypeError:
    #     print("Must be between 33 and 127")
    except ValueError:
        print("Must be an integer")




def convert_character_to_ascii(character):
    ascii_value = ord(character)
    return ascii_value

def convert_integer_to_character(number):
    integer_as_character = chr(number)
    return integer_as_character


main()