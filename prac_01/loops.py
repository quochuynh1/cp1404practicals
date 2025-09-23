# for loop that displays all the odd numbers between 1 and 20 with a space between each one
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# # a. count in 10s from 0 to 100
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# # b. count down from 20 to 1
for i in range(20,0, -1):
    print(i, end=' ')
print()

# c. print a number of stars
number_of_stars = int(input("how many stars would you like to print?:"))
for number in range(number_of_stars):
    print("*", end=" ")
print()

# d. print lines of increasing stars
number_of_lines = int(input("Enter the number of lines: "))
for line in range(1, number_of_lines + 1):
    print("*" * line)
print()


