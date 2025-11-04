"""
Prac 05 Extension - Name and Address
"""

FILENAME = "addresses.csv"

def main():
    """Write a program that uses a dictionary to store and look up your friends' names and addresses.
    Assume you don't have many friends :) and none of them share the same name (this means the name
    can be the unique key for the dictionary)."""

    name_to_address = load_data()

    print("[E]nter a new name and address")
    print("[C]hange an address for an existing entry")
    print("[P]rint the address for a name you choose")
    print("[S]ave data")
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
        elif choice == "S":
            save_data(name_to_address)
            print("Data Saved.")
        else:
            print("Invalid Choice")
        print("[E]nter a new name and address")
        print("[C]hange an address for an existing entry")
        print("[P]rint the address for a name you choose")
        print("[S]ave data")
        choice = input(">>> ").upper()


def load_data():
    """Load name/address pairs from a file, if it exists."""
    name_to_address = {}
    try:
        with open(FILENAME, "r", encoding="utf-8") as in_file:
            for line in in_file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    name, address = parts
                    name_to_address[name] = address
        print(f"Loaded {len(name_to_address)} entries from {FILENAME}.")
    except FileNotFoundError:
        print(f"No existing data found. Starting fresh.")
    return name_to_address


def save_data(name_to_address):
    """Save all name/address pairs to a file."""
    with open(FILENAME, "w") as out_file:
        for name, address in name_to_address.items():
            print(f"{name},{address}", file=out_file)


def get_name_and_address(name_to_address):
    """"""
    name = input("Enter name: ").title()
    address = input("Enter address: ").title()

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
