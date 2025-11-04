"""
Prac 06 Practice - Persons
"""


class Person:
    def __init__(self, first_name="", last_name="", age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age}"

    def __repr__(self):
        return str(self)


def main():
    people = [Person("Alex", "Huynh", 20), Person("James", "Smith", 34)]
    first_name = input("First name: ")
    while first_name != "":
        last_name = input("Last name: ")
        age = int(input("Age: "))

        person = Person(first_name, last_name, age)
        people.append(person)

        first_name = input("First name: ")

    print("\n{:<12}{:<12}{:>3}".format("First name", "Last name", "Age"))
    print("-" * 30)
    for person in people:
        print(person)


main()
