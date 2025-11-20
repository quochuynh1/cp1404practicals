"""
Prac 09 - UnreliableCar tests
"""

from unreliable_car import UnreliableCar

test_car = UnreliableCar("Test", fuel=1000, reliability=30)

success_count = 0

for i in range(100):
    distance_driven = test_car.drive(1)
    if distance_driven > 0:
        success_count += 1

print(f"Testing a car with 30% reliability")
print(f"Out of 100 attempts, the test car drove {success_count} times.")
