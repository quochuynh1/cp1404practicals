"""
Prac 06 - Testing Guitar class
"""
from prac_06.guitar import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 16035.40)

print(guitar1)
print(guitar2)

print(guitar1.get_age())
print(guitar2.get_age())

print(guitar1.is_vintage())
print(guitar2.is_vintage())

guitars = [guitar1, guitar2]

print(f"{guitar1.name} get_age() - Expected 100. Tot {guitar1.get_age()}")
print(f"{guitar2.name} get_age() - Expected 9. Got {guitar2.get_age()}")

print(f"{guitar1.name}  is_vintage() - Expected True. got {guitar1.is_vintage()}")
print(f"{guitar2.name}  is_vintage() - Expected False. got {guitar2.is_vintage()}")
