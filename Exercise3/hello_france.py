items = input().split("|")
budget = float(input())

bought_items_values = []
profit = 0
TICKET_PRICE = 150

for item in items:
    item_type, item_price = item.split("->")
    item_price = float(item_price)

    if (item_type == "Clothes" and item_price <= 50     # clothes maximum price
            or item_type == "Shoes" and item_price <= 35    # shoes maximum price
            or item_type == "Accessories" and item_price <= 20.50):     # accessories maximum price
        if budget >= item_price:
            budget -= item_price
            bought_items_values.append(item_price * 1.4)    # 40% sales margin
            profit += 0.4 * item_price
            print(f"{1.4 * item_price:.2f} ", end="")
print("\n"f"Profit: {profit:.2f}")

budget += sum(bought_items_values)

print("Hello, France!" if budget >= TICKET_PRICE else "Not enough money.")
