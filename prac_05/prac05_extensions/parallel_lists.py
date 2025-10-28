"""
Prac 5 Extension - Parallel Lists
"""


def main():
    """"""
    names = ["Jack", "Jill", "Harry"]
    dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]

    dictionary = make_dictionary(names, dates_of_birth)
    print(dictionary)


def make_dictionary(key, value):
    """"""
    dictionary = {key: value for key, value in zip(key, value)}
    return dictionary


main()
