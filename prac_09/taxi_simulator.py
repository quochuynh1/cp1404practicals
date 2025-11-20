"""
Prac 09 - Taxi Simulator
"""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi


def main():
    """Taxi simulator program"""

    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    print("Let's Drive!")
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = get_valid_taxi(current_taxi, taxis)
        elif choice == "D":
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").upper()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now: ")
    display_taxis(taxis)


def display_taxis(taxis):
    """Displayed taxis with their corresponding number"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_taxi(current_taxi, taxis):
    """Get a valid taxi choice"""
    try:
        taxi_choice = int(input("Choose taxi: "))
        current_taxi = taxis[taxi_choice]
    except (ValueError, IndexError):
        print("Invalid taxi choice")
    return current_taxi


def drive_taxi(current_taxi, total_bill):
    """Drive current taxi and update the total bill accordingly"""
    if current_taxi:
        current_taxi.start_fare()
        distance = float(input("Drive how far? "))
        current_taxi.drive(distance)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        total_bill += trip_cost
    else:
        print("You need to choose a taxi before you can drive")
    return total_bill


main()
