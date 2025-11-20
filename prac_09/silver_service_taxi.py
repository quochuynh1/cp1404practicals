"""
Prac 09 - SilverServiceTaxi
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of Taxi"""

    flagfall = 4.5  # Class variable for extra charge

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise a SilverServiceTaxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Override other methods to calculate fare"""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """String representation of SilverServiceTaxi"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
