"""Program to ask for 5 numbers, store them in a list, then output information about the numbers"""

numbers = []
for i in range(1, 6):
    user_numbers = int(input("Numbers: "))
    numbers.append(user_numbers)


print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")

average_number = sum(numbers) / len(numbers)
print(f"The average of the numbers is {average_number}")


"""Woefully inadequate security checker"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

input_username = input("Enter Username: ")

if input_username in usernames:
    print("Access granted")
else:
    print("Access denied")

