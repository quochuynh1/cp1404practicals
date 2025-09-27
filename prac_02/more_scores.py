"""Docstring"""

import random


def main():
    """"""
    number_of_scores = get_number_of_scores()
    for i in range(number_of_scores):
        random_score = assign_random_score(number_of_scores)
        print(f"{random_score} is:", categorise_score(random_score))


def get_number_of_scores():
    """"""
    number_of_scores = int(input("Number of Scores:"))
    return number_of_scores


def assign_random_score(number_of_scores):
    """"""
    for i in range(number_of_scores):
        random_score = random.randint(0, 100)
    return random_score


def categorise_score(random_score):
    """Sort the given score (parameter) into categories with error checking"""
    if random_score < 0 or random_score > 100:
        return "Invalid Score"
    elif random_score >= 90:
        return "Excellent"
    elif random_score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
