number_of_items = int(input("Enter number of items: "))
price_of_items = 0
total_price = 0
while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Enter number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Enter price of items: "))
    total_price += price_of_item
    if total_price > 100:
        total_price = total_price * 0.9
print(f"Total price for {number_of_items} items: {total_price:.2f}")


