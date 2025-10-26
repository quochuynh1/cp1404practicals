"""
Prac 05 Practice - Friends
"""


def main():
    """Write a program that uses a dictionary to store and look up your friends' names and addresses.
    Assume you don't have many friends :) and none of them share the same name (this means the name
    can be the unique key for the dictionary)."""
    name_to_address = {"Alex": "Smithfield", "Toby": "Caravonica"}

    print("[E]nter a new name and address")
    print("[C]hange an address for an existing entry")
    print("[P]rint the address for a name you choose")
    choice = input(">>> ").upper()
    while choice != "":
        if choice == "E":
            name_to_address = get_name_and_address(name_to_address)
            print(name_to_address)
        elif choice == "C":
            name_to_address = change_address(name_to_address)
            print(name_to_address)
        elif choice == "P":
            print_address(name_to_address)
        choice = input(">>> ").upper()


def get_name_and_address(name_to_address):
    """"""
    name = input("Enter name: ").upper()
    address = input("Enter address: ").upper()

    name_to_address[name] = address
    return name_to_address

def change_address(name_to_address):
    """"""
    name = input("Enter name of the friend's address you want to change: ").title()
    if name in name_to_address:
        address = input("Enter new address: ").upper()
        name_to_address[name] = address
    else:
        print("Name not found")
    return name_to_address

def print_address(name_to_address):
    name = input("Enter name of address you want to print: ").title()
    if name in name_to_address:
        print(f"{name} lives at: {name_to_address[name]}")
    else:
        print("Name not found")



main()
