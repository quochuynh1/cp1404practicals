
# Electricity bill calculator

price_per_kwh = float(input("Enter price per kwh in cents: "))
daily_use = float(input("Enter daily use in kWh:"))
number_of_billing_days = int(input("Enter number of billing days:"))
while daily_use and number_of_billing_days >= 0:
    estimated_bil = (number_of_billing_days * daily_use * price_per_kwh) / 100
    print(f"Estimated Bill: {estimated_bil:.2f}")
    price_per_kwh = float(input("Enter price per kwh in cents: "))
    daily_use = float(input("Enter daily use in kWh:"))
    number_of_billing_days = int(input("Enter number of billing days:"))



# Electricity bill calculator 2.0

# Define constants
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff = int(input("Which tarrif? 11 or 31:"))
daily_use = float(input("Enter daily use in kWh:"))
number_of_billing_days = int(input("Enter number of billing days:"))
while daily_use and number_of_billing_days >= 0:
    estimated_bil = (number_of_billing_days * daily_use)
    if tariff == 11:
        estimated_bil *= TARIFF_11
    elif tariff == 31:
        estimated_bil *= TARIFF_31
    print(f"Estimated Bill: {estimated_bil:.2f}")
    tariff = int(input("Which tarrif? 11 or 31:"))
    daily_use = float(input("Enter daily use in kWh:"))
    number_of_billing_days = int(input("Enter number of billing days:"))
