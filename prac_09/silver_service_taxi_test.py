"""
Prac 09 - Testing SilverServiceTaxi
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Hummer", fuel=100, fanciness=3)

taxi.start_fare()
taxi.drive(18)

print(taxi)
fare = taxi.get_fare()

assert abs(fare - 48.78) < 0.01, f"Fare should be $48.78, got{fare:.2f}"
