number = int(input())

for num in range(1, number + 1):
    digits_sum = 0
    digits = num
    while digits > 0:
        digits_sum += digits % 10
        digits = int(digits / 10)

    if digits_sum in [5, 7, 11]:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
