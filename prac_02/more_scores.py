"""Program to print random results based on number of scores given by user"""

import random


def main():
    """print the random score and result"""
    number_of_scores = get_number_of_scores()
    for i in range(number_of_scores):
        random_score = assign_random_score(number_of_scores)
        print(f"{random_score} is:", categorise_score(random_score))


def get_number_of_scores():
    """ask the user how many scores they would like to print"""
    number_of_scores = int(input("Number of Scores:"))
    return number_of_scores


def assign_random_score(number_of_scores):
    """assign however many scores are needed with a random score"""
    for i in range(number_of_scores):
        random_score = random.randint(0, 100)
    return random_score


def categorise_score(random_score):
    """Sort the random score into categories with error checking"""
    if random_score >= 90:
        return "Excellent"
    elif random_score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
