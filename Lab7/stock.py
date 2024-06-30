stock = input().split()
bakery = {}

for i in range(0, len(stock), 2):
    bakery[stock[i]] = int(stock[i + 1])

products_searched = input().split()

for product in products_searched:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
