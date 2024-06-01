divisor = int(input())
boundary = int(input())
maximum = 0

for number in range(0, boundary + 1):
    if number % divisor == 0:
        maximum = number

print(maximum)
