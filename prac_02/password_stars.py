"""ask user for password, print asterisks as long as password"""

password = input("Password:")
password_length = len(password)

if password == "":
    print("Password can't be empty")
else:
    for i in range(password_length):
        print("*", end="")



