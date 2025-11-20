"""
Prac 09 - Taxi Simulator
"""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi


def main():
    """Taxi simulator program"""

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's Drive!")
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            pass
        elif choice == "D":
            pass
        else:
            print("Invalid option")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").upper()


main()
