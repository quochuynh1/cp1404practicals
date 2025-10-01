"""Program answering the questions in 'Files' section of practical 3"""

# 1
name = input("Name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# 2
in_file = open("name.txt", "r")
print(f"Hi {in_file.read()}!")
in_file.close()

# 3
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline().strip())
    second_number = int(in_file.readline().strip())
    result = first_number + second_number
    print(f"Sum of first two lines is: {result}")

# 4
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        number = int(line.strip())
        total += number
    print(f"Sum of all numbers in 'numbers.txt' is: {total}")
