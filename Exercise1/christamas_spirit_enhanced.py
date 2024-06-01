decoration_qty = int(input())
days_left = int(input())

decorations = {
    "ornament": {"price": 2, "points": 5, "quantity": 0},
    "skirt": {"price": 5, "points": 3, "quantity": 0},
    "garland": {"price": 3, "points": 10, "quantity": 0},
    "light": {"price": 15, "points": 17, "quantity": 0}
}
spirit_points = 0

for day in range(1, days_left + 1):
    if day % 11 == 0:
        decoration_qty += 2
    if day % 2 == 0:
        decorations["ornament"]["quantity"] += decoration_qty
        spirit_points += decorations["ornament"]["points"]
    if day % 3 == 0:
        decorations["skirt"]["quantity"] += decoration_qty
        decorations["garland"]["quantity"] += decoration_qty
        spirit_points += decorations["skirt"]["points"] + decorations["garland"]["points"]
    if day % 5 == 0:
        decorations["light"]["quantity"] += decoration_qty
        spirit_points += decorations["light"]["points"]
    if day % 5 == 0 and day % 3 == 0:
        spirit_points += 30
    if day % 10 == 0:
        spirit_points -= 20
        decorations["skirt"]["quantity"] += 1
        decorations["garland"]["quantity"] += 1
        decorations["light"]["quantity"] += 1
        if day == days_left:
            spirit_points -= 30

total_cost = sum(item["quantity"] * item["price"] for item in decorations.values())

print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit_points}")
