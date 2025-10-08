"""Program to automatically generate a password"""

import random

# SPEACIAL_CHARACTERS = "!@#$%^&*()_+?/.>,<|\{}[]~`"
LETTERS = "abcdefghijklmnopqrstuvwrxyz"

try:
    number_of_upper = int(input("Enter required number of Upper case letters: "))
    number_of_lower = int(input("Enter required number of Lower case letters: "))
    number_of_numbers = int(input("Enter required number of Numbers: "))
    # number_of_speacial = int(input("Enter required number of Speacial characters: "))
    password = ""
    for i in number_of_upper, number_of_lower:
        password += random.choice(LETTERS)
        print(password)
except ValueError:
    print("Invalid Input")