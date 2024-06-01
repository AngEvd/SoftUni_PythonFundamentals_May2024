cells = input().split("#")
water = int(input())

effort, total_fire = 0, 0

print("Cells:")

for cell in cells:
    fire_type, fire_level = cell.split(" = ")
    fire_level = int(fire_level)
    if fire_type == "High" and 81 <= fire_level <= 125\
            or fire_type == "Medium" and 51 <= fire_level <= 80\
            or fire_type == "Low" and 1 <= fire_level <= 50:
        if water >= fire_level:
            water -= fire_level
            effort += 0.25 * fire_level
            total_fire += fire_level
            print(f"- {fire_level}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
