"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():
    word_format = is_valid_format()
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    print(word)


def is_valid_format():
    is_valid_input = False
    while not is_valid_input:
        try:
            word_format = input("Enter a sequence of vowels and constants (e.g., ccvcvvc): ")
            if all(kind in ('c', 'v') for kind in word_format):
                return word_format
            else:
                print("Invalid Input")
        except ValueError:
            print("Enter either c or v")
    return None




main()
