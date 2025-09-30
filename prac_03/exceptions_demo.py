"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError will occur on line 12 OR 13 if the user were to input something other than an integer (including leaving it empty) into numerator or denominator.
2. When will a ZeroDivisionError occur?
    A ZeroDivisionError will occur on line 14 if the user were to input 0 into the denominator on line 13 and the fraction will try to divide by zero before raising the error.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Replace the ZeroDivisionError exception with a denominator input validation error checking while loop which repeatedly asks for a denominator until a non-zero is entered.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")