"""
Prac 09 - Band
"""


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician collection"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band"""
        musicians_string = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_string})"

    def __repr__(self):
        """Return a string representation of a Band, showing the verbalises"""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to musicians collection"""
        self.musicians.append(musician)

    def play(self):
        """Tell the musician to play their instrument (if they have one)"""
        for musician in self.musicians:
            print(musician.play())
