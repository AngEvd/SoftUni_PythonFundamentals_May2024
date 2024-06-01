lost_fights = int(input())
helmet_price, sword_price, shield_price, armor_price = float(input()), float(input()), float(input()), float(input())

expenses = 0
broken_shields = 0

for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:  # every second fight helmet is broken
        expenses += helmet_price
    if fight % 3 == 0:   # every third fight sword is broken
        expenses += sword_price
    if fight % 6 == 0:  # when helmet and sword are broken together, shield is also broken
        expenses += shield_price
        broken_shields += 1
        if broken_shields % 2 == 0:
            expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
