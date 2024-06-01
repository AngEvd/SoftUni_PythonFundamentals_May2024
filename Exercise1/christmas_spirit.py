decoration_qty = int(input())
days_left = int(input())

ornaments, skirts, garlands, lights, spirit_points = 0, 0, 0, 0, 0

ornament = {"price": 2, "points": 5}
skirt = {"price": 5, "points": 3}
garland = {"price": 3, "points": 10}
light = {"price": 15, "points": 17}

for day in range(1, days_left + 1):
    if day % 11 == 0:
        decoration_qty += 2
    if day % 2 == 0:
        ornaments += decoration_qty
        spirit_points += ornament["points"]
    if day % 3 == 0:
        skirts += decoration_qty
        garlands += decoration_qty
        spirit_points += skirt["points"] + garland["points"]
    if day % 5 == 0:
        lights += decoration_qty
        spirit_points += light["points"]
    if day % 5 == 0 and day % 3 == 0:
        spirit_points += 30
    if day % 10 == 0:
        spirit_points -= 20
        skirts += 1
        garlands += 1
        lights += 1
        if day == days_left:
            spirit_points -= 30

total = (ornaments * ornament["price"] +
         skirts * skirt["price"] +
         garlands * garland["price"] +
         lights * light["price"])

print(f"Total cost: {total}")
print(f"Total spirit: {spirit_points}")
