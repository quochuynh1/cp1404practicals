"""Ask user for password of minimum characters, print asterisks as many asterisks as the length of password"""

MINIMUM_CHARACTERS = 5


def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    """Get password and validate that it is at least 5 characters long"""
    password = input("Enter password of at least 5 characters:")
    while len(password) < MINIMUM_CHARACTERS:
        print("Password must be at least 5 characters")
        password = input("Enter password of at least 5 characters:")
    return password


def print_asterisks(password):
    for i in range(len(password)):
        print("*", end="")


main()
