"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# 4. Write a loop that prints all the states and names neatly lined up with string formatting

max_length = max(len(state_code) for state_code in list(CODE_TO_NAME.keys()))

for state_code in CODE_TO_NAME.keys():
    state_name = CODE_TO_NAME[state_code]
    print(f"{state_code:{max_length}} is {state_name}")
print()

# 5. This code uses the "Look Before You Leap" (LBYL) approach to checking if the key is in the dictionary.
#    Change this to use exceptions and the "Easier to Ask Forgiveness than Permission" (EAFP) approach.

max_length = max(len(state_code) for state_code in CODE_TO_NAME.keys())

for state_code in CODE_TO_NAME.keys():
    try:
        state_name = CODE_TO_NAME[state_code]
        print(f"{state_code:{max_length}} is {state_name}")
    except KeyError:
        print(f"No state name found for code '{state_code}'")
