stock = input().split()
bakery = {}

for i in range(0, len(stock), 2):
    bakery[stock[i]] = int(stock[i + 1])

print(bakery)