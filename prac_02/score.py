"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random


def main():
    """Get score from user and print the category of score (result)"""
    random_score = random.randint(0, 100)
    print("Your random score was: ", random_score, "and \n")
    print("Your random score is:", categorise_score(random_score))


def categorise_score(random_score):
    """Sort the given score (parameter) into categories with error checking"""
    if random_score < 0 or random_score > 100:
        return "Invalid Score"
    elif random_score >= 90:
        return "excellent"
    elif random_score >= 50:
        return "passable"
    else:
        return "bad"


main()
