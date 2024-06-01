budget = float(input())
flour_kg_price = float(input())

egg_pack_price = 0.75 * flour_kg_price
milk_liter_price = 1.25 * flour_kg_price
current_bread_count = 0
colored_eggs_count = 0

bread_price = egg_pack_price + flour_kg_price + 0.25 * milk_liter_price

while True:
    if budget > bread_price:
        budget -= bread_price
        current_bread_count += 1
        colored_eggs_count += 3
        if current_bread_count % 3 == 0:
            colored_eggs_count -= current_bread_count - 2
    else:
        break

print(f"You made {current_bread_count} loaves of Easter bread!"
      f" Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")
