"""
Program that asks the user how many "quick picks" they wish to generate.
The program then generates that many lines of output.
Each line consists of 6 random numbers between 1 and 45.
"""

import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
LENGTH_OF_PICK = 6

def main():
    """Program to generate however many quick picks the user inputs"""
    number_of_picks = 20 # int(input("How many quick picks?: "))

    for i in range(number_of_picks):
        quick_pick = []
        while len(quick_pick) < LENGTH_OF_PICK:
            random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            while random_number in quick_pick: # if number is already in quick_pick list, choose another random number
                random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            quick_pick.append(random_number) # keep adding random numbers to quick_pick until the
            quick_pick.sort() # print in ascending order
        print(" ".join(f"{random_number:2}" for random_number in quick_pick))

main()



