numbers = [int(number) for number in input().split()]
k = int(input())

index = 0
killed = []

while numbers:
    index = (index + k - 1) % len(numbers)
    killed.append(numbers.pop(index))

print(str(killed).replace(" ", ""))
