numbers = input().split()

time_left, time_right = 0, 0

mid = len(numbers) // 2

for number in numbers[:mid]:
    if int(number) == 0:
        time_left *= 0.8
    else:
        time_left += int(number)

for number in numbers[mid+1:][::-1]:
    if int(number) == 0:
        time_right *= 0.8
    else:
        time_right += int(number)

winner = "left" if time_left < time_right else "right"
times = {"left": time_left, "right": time_right}

print(f"The winner is {winner} with total time: {times.get(winner):.1f}")

