"""Program to simulate gopher population"""

import random


def main():
    print("Welcome to the Gopher Population Simulator!")
    print("Starting population: 1000")
    print("Year 1")

    for i in range(11):
        gopher_births = generate_random_gopher_birth()
        gopher_deaths = generate_random_gopher_death()
        SECRET_POPULATION = 1000

        print(f"{gopher_births} gophers were born. {gopher_deaths} died.")
        SECRET_POPULATION = SECRET_POPULATION + gopher_births - gopher_deaths
        print(f"New population: {SECRET_POPULATION}")
        print("Year", i)
        print()


def generate_random_gopher_birth():
    SECRET_POPULATION = 1000
    lower_limit_birth = int(SECRET_POPULATION * 0.1)
    upper_limit_birth = int(SECRET_POPULATION * 0.2)

    gopher_births = random.randint(lower_limit_birth, upper_limit_birth)
    return gopher_births


def generate_random_gopher_death():
    SECRET_POPULATION = 1000
    lower_limit_death = int(SECRET_POPULATION * 0.05)
    upper_limit_death = int(SECRET_POPULATION * 0.25)

    gopher_death = random.randint(lower_limit_death, upper_limit_death)
    return gopher_death


main()
