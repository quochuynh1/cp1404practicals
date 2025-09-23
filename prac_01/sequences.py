
# Show menu
print("(E)ven number sequence")
print("(O)dd number sequence")
print("(S)quared number sequence")
print("(Q)uit")
choice = str(input(">>>"))
print()

while choice != "Q":
    if choice == "E":
        even_start = int(input("Enter even start value"))
        if even_start % 2 != 0:
            print("Please enter even number")
            even_start = int(input("Enter even start value"))
        even_end = int(input("Enter even end value"))
        for i in range(even_start, even_end + 1, 2):
            print(i, end=" ")
        choice = str(input("\n>>>"))
    elif choice == "O":
        odd_start = int(input("Enter odd start value"))
        if odd_start % 2 == 0:
            print("Please enter odd number")
            odd_start = int(input("Enter odd start value"))
        odd_end = int(input("Enter odd end value"))
        for i in range(odd_start, odd_end + 1, 2):
            print(i, end=" ")
        choice = str(input("\n>>>"))
    else:
        print("Invalid Input")
        print("(E)ven number sequence")
        print("(O)dd number sequence")
        print("(S)quared number sequence")
        print("(Q)uit")
        choice = str(input(">>>"))
        print()
print("Finished")