products = {}

while True:
    input_line = input()
    if input_line == "buy":
        break
    else:
        name, price, quantity = input_line.split()
        if name not in products:
            products[name] = 0
            products[name] = {"price": float(price), "quantity": int(quantity)}
        else:
            products[name]["quantity"] += int(quantity)
            products[name]["price"] = float(price)


for product_name, product_info in products.items():
    print(f"{product_name} -> {product_info['price'] * product_info['quantity']:.2f}")
