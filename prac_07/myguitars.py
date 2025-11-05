"""
Prac 07 - More Guitars
"""
from prac_07.guitar import Guitar


def main():
    """Guitar Program"""
    guitars = load_guitars()
    print_guitars(guitars)
    get_new_guitars(guitars)
    save_new_guitars(guitars)


def load_guitars():
    """Read the guitars.csv file and store each record as a Guitar object in a list"""
    guitars = []
    with open("guitars.csv", "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
        return guitars


def print_guitars(guitars):
    """Print guitars sorted by year"""
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def get_new_guitars(guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")

        name = input("Name: ")
    return guitars


def save_new_guitars(guitars):
    with open("guitars.csv", "w") as out_file:
        guitars.sort()
        for guitar in guitars:
            out_file.write(f"{guitar.name}, {guitar.year}, {guitar.cost}\n")


main()
