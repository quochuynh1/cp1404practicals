"""Main menu to get valid score, print result, and show stars"""


def main():
    """Take user input based on the menu prompts and reject other inputs"""
    print("Menu:")
    print("Press [G] to Get a valid score (must be 0-100)")
    print("Press [P] to Print the result")
    print("Press [S] to Show stars")
    print("Press [Q] to Quit")
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print()
        elif choice == "P":
            print(f"Your score {score} is:", categorise_score(score))
            print()
        elif choice == "S":
            print_asterisks(score)
            print("\n")
        else:
            print("Invalid input")
        print("Menu:")
        print("Press [G] to Get a valid score (must be 0-100)")
        print("Press [P] to print the result")
        print("Press [S] to show stars")
        print("Press [Q] to Quit")
        choice = input("> ").upper()
    print(f"Quitting Program...")


def get_valid_score():
    """Check that the score is between 0-100 and return the score"""
    score = int(input("Enter Score:"))
    while score < 0 or score > 100:
        print("Score must be between 0-100")
        score = int(input("Enter Score:"))
    return score


def categorise_score(score):
    """Sort the given score (parameter) into categories with error checking"""
    if score >= 90:
        return "excellent"
    elif score >= 50:
        return "passable"
    else:
        return "bad"


def print_asterisks(score):
    """Print as many asterisks as the score"""
    for i in range(score):
        print("*", end="")


main()
