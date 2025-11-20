"""
Prac 09 - UnreliableCar class
"""
import random

from prac_06.car import Car


class UnreliableCar(Car):
    """Specialised version of Car"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if the random number is < reliability"""
        random_number = random.randint(0, 100)

        if random_number < self.reliability:
            return super().drive(distance)
        else:
            return 0
