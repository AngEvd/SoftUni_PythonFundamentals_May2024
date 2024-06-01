n = int(input())

capacity = 255
water_in_tank = 0

for i in range(n):
    water_poured = int(input())
    if water_poured <= capacity - water_in_tank:
        water_in_tank += water_poured
    else:
        print("Insufficient capacity!")

print(water_in_tank)

