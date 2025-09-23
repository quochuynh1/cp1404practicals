"""Ask user for password of minimum characters, print asterisks as many asterisks as the length of password"""

MINIMUM_CHARACTERS = 5

password = input("Enter password of at least 5 characters:")

while len(password) < MINIMUM_CHARACTERS:
    print("Password must be at least 5 characters")
    password = input("Enter password of at least 5 characters:")
for i in range(len(password)):
    print("*", end="")
