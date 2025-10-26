# Electricity bill calculator 3.0

# Define constants
TARRIF_TO_COST = {11: 0.244618, 21: 0.6767676, 31: 0.136928, 41: 0.696969}

print(TARRIF_TO_COST)
tariff = int(input("Which tarrif?: "))
daily_use = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
while daily_use and number_of_billing_days >= 0:
    estimated_bil = (number_of_billing_days * daily_use)
    # if tariff == 11:
    #     estimated_bil *= TARIFF_11
    # elif tariff == 31:
    #     estimated_bil *= TARIFF_31
    estimated_bil *= TARRIF_TO_COST[tariff]
    print(f"Estimated Bill: {estimated_bil:.2f}")
    tariff = int(input("Which tarrif? 11 or 31:"))
    daily_use = float(input("Enter daily use in kWh:"))
    number_of_billing_days = int(input("Enter number of billing days:"))