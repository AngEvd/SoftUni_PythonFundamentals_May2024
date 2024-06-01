import math

is_prime = True
number = int(input())

for num in range(2, int(math.sqrt(number)) + 1):
    if number % num == 0:
        is_prime = False
        break

print(is_prime)
