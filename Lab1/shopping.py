budget = int(input())

while budget >= 0:
    price = input()
    if price == "End":
        exit(print("You bought everything needed."))
    else:
        budget -= int(price)

print("You went in overdraft!")
