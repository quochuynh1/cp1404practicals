"""
CP1404/CP5632 - Practical
Program to determine score status
"""


def main():
    """Get score from user and print the category of score (result)"""
    score = float(input("Enter score: "))
    print("Your score is:", categorise_score(score))


def categorise_score(score):
    """Sort the given score (parameter) into categories with error checking"""
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "excellent"
    elif score >= 50:
        return "passable"
    else:
        return "bad"


main()
