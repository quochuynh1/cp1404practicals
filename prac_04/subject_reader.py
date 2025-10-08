"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data(FILENAME)
    print(data)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    result = []

    for line in input_file:
        parts = line.strip().split(',')
        parts[2] = int(parts[2])
        result.append(parts)

    input_file.close()
    return result


main()
