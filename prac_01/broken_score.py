"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score < 50:
    value = "bad"
elif score < 90:
    value = "passable"
else:
    value = "excellent"
print(f"your score {score} is {value}")



