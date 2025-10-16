"""
Wimbledon
Estimated:
Actual
"""

FILENAME = "wimbledon.csv"


def main():
    """Program to read Wimbledon data and display processed information"""

    data = read_data(FILENAME)
    champion_to_count, countries = extract_information(data)
    display_information(champion_to_count, countries)


def read_data(filename):
    """Read the data from wimbldon.csv and store it in a list of lists"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        data = [line.strip().split(",") for line in in_file]
        return data


def extract_information(data):
    """Create dictionary mapping champion to how many times they've been champion (i.e., count).
    Create set for all the countries that have won.
    """

    champion_to_count = {}
    countries = set()

    for record in data:
        country = record[1]
        champion = record[2]

        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
        countries.add(country)

    return champion_to_count, countries


def display_information(champion_to_count, countries):
    """Display champion mapped to count and countries that have won (alphabetical order)"""
    for champ in champion_to_count:
        print(f"{champ} {champion_to_count[champ]}")

    print(f"These {len(countries)} have won Wimbledon:")
    print(" ".join(sorted(countries)))


main()
