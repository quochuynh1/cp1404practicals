"""
Prac 09 - Testing SilverServiceTaxi
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Hummer", fuel=100, fanciness=2)

taxi.start_fare()
taxi.drive(18)

print(taxi)
fare = taxi.get_fare()
print(f"${fare:.2f}")

assert abs(fare - 48.78) < 0.1, f"Fare should be $48.78, got{fare:.2f}"
