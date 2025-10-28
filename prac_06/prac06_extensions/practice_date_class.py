"""Prac 6 Extension - Date"""
from datetime import date, timedelta


class Date:
    def __init__(self, day=24, month=12, year=2004):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"

    def add_days(self, n):
        current_date = date(self.year, self.month, self.day)
        new_date = current_date + timedelta(days=n)

        self.day, self.month, self.year = new_date.day, new_date.month, new_date.year


def main():
    birthday = Date()
    print(birthday)
    birthday.add_days(50)
    print(f"Birthday after 50 days: {birthday}")


main()
