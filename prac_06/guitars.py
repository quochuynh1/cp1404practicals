"""
Prac 06 - Playing with Guitars
Estimated: 1hr
Actual: 1hr 20mins
"""

from prac_06.guitar import Guitar

guitars = [Guitar("Fender Stratocaster", 2014, 765.40), Guitar("Gibson L-5 CES", 1922, 16035.40),
           Guitar("Line 6 JTV-59", 2010, 1512.90)]

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))

    guitar_data = Guitar(name, year, cost)
    guitars.append(guitar_data)
    print(f"{guitar_data} added.")

    name = input("Name: ")

print()
print("... snip ...")
print()

max_name_length = max(len(guitar.name) for guitar in guitars)
max_cost_length = max(len(str(guitar.cost)) for guitar in guitars)

for guitar_number, guitar in enumerate(guitars, 1):
    if guitar.is_vintage():
        print(
            f"Guitar {guitar_number}: {guitar.name:>{max_name_length}} ({guitar.year}), worth $ {guitar.cost:>{max_cost_length + 2},.2f} (vintage)")
    else:
        print(
            f"Guitar {guitar_number:}: {guitar.name:>{max_name_length}} ({guitar.year}), worth $ {guitar.cost:>{max_cost_length + 2},.2f}")
