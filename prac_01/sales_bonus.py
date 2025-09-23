"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: "))
if sales >= 0 and sales < 1000:
    bonus = sales * 0.10
    print(f"Bonus: {bonus}")
elif sales >= 1000:
    bonus = sales * 0.15
    print(f"Bonus: {bonus}")
else:
    print("invalid input")
    sales = float(input("Enter sales: "))



sales = float(input("Enter sales: "))
total_bonus = 0
total_sales = 0
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
        total_sales += sales
        total_bonus += bonus
        sales = float(input("Enter sales: "))
    elif sales >= 1000:
        bonus = sales * 0.15
        total_sales += sales
        total_bonus += bonus
        sales = float(input("Enter sales: "))
else:
    print(f"Bonus from {total_sales} is bonus {total_bonus}")





