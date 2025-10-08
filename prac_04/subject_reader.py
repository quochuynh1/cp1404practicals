"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_records = load_subject_records(FILENAME)
    print(subject_records)
    print_subject_details(FILENAME)


def load_subject_records(filename=FILENAME):
    """Separate records into parts and then load them into one record in the form of a nested list"""
    input_file = open(filename)
    record = []

    for line in input_file:
        parts = line.strip().split(',')
        parts[2] = int(parts[2])
        record.append(parts)
    input_file.close()
    return record


def print_subject_details(filename=FILENAME):
    """Display all subject details"""
    input_file = open(filename)

    for line in input_file:
        parts = line.strip().split(',')
        subject = parts[0]
        lecturer = parts[1]
        number_of_students = parts[2]
        print(f"{subject} is taught by {lecturer} and has {number_of_students} students")
    input_file.close()


main()
