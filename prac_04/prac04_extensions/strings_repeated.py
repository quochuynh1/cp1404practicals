"""
Prac 04 Practice - 3. Strings repeated
"""


def main():
    """Program that asks the user for an indefinite set of strings - until
    an empty string is entered - then prints all of the strings that were
    entered more than once."""
    repeated_strings = get_strings()
    print_repeated_strings(repeated_strings)

def get_strings():
    """Asks the user for an indefinite set of strings and stores them in a list called strings"""
    strings = []
    repeated_strings = []
    string = input("Enter String: ")
    while string != "":
        if string in strings:
            repeated_strings.append(string)
        else:
            strings.append(string)
        string = input("Enter String: ")
    return repeated_strings

def print_repeated_strings(repeated_strings):
    """Print the repeated strings"""
    string_output = ",".join(repeated_strings)
    print(f"Strings repeated: {string_output}")



main()
