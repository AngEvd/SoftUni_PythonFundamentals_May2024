orders_number = int(input())

total_price = 0

for _ in range(orders_number):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 0.01 <= capsule_price <= 100 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        price = days * capsules_per_day * capsule_price
        total_price += price
        print(f"The price for the coffee is: ${price:.2f}")
    else:
        continue

print(f"Total: ${total_price:.2f}")