"""
Prac 06 Practice - Driving Simulator
"""

from prac_06.car import Car


def main():
    """Driving Simulator Program"""
    print("Let's drive!")
    car = Car("The bomb", 100, 0)
    print(car)

    print()
    print("Menu:")
    print("(d) drive")
    print("(r) refuel")
    print("(q) quit")
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "D":
            drive_car(car)
        elif choice == "R":
            refuel_car(car)
        else:
            print("Invalid choice")
        print()
        print(car)
        print("Menu:")
        print("(d) drive")
        print("(r) refuel")
        print("(q) quit")
        choice = input("Enter your choice: ").upper()


def drive_car(car):
    """Drive car"""
    is_valid_input = False
    while not is_valid_input:
        try:
            distance = int(input("How many km do you wish to drive? "))
            if distance <= 0:
                print("Distance must be >= 0")
            else:
                distance_driven = car.drive(distance)
                if distance_driven < distance:
                    print(f"The car drove {distance_driven} and ran out of fuel")
                else:
                    print(f"The car drove {distance_driven}km")
                is_valid_input = True
        except ValueError:
            print("Invalid input")
    return distance_driven


def refuel_car(car):
    """Add fuel to car"""
    is_valid_input = False
    while not is_valid_input:
        try:
            amount_of_fuel = int(input("How many units of fuel d you want to add too the car? "))
            if amount_of_fuel <= 0:
                print("Fuel amount must be >= 0")
            else:
                car.add_fuel(amount_of_fuel)
                print(f'Added {amount_of_fuel} units of fuel')
                is_valid_input = True
        except ValueError:
            print("Invalid input")


main()
