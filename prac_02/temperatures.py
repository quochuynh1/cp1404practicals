"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""
from prac_01.temperatures import celsius, fahrenheit

def main():
    MENU = """C - Convert Celsius to Fahrenheit
        F - Convert Fahrenheit to Celsius
        Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            convert_to_fahrenheit()
        elif choice == "F":
            convert_to_celcius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_fahrenheit():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


def convert_to_celcius():
    global fahrenheit, celsius
    fahrenheit = float(input("Fahrenheit : "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


main()
