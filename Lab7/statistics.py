bakery = {}

while True:
    command = input()
    if command == "statistics":
        break
    else:
        product, quantity = command.split(": ")
        if product not in bakery:
            bakery[product] = 0
        bakery[product] += int(quantity)

print("Products in stock:")
for product in bakery:
    print(f"- {product}: {bakery[product]}")
print(f"Total Products: {len(bakery.keys())}")
print(f"Total Quantity: {sum(bakery.values())}")
