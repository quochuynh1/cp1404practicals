"""
Prac 07 - More Guitars
"""
from prac_07.guitar import Guitar


def main():
    """Guitar Program"""
    guitars = load_guitars()
    print_guitars(guitars)


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


main()
