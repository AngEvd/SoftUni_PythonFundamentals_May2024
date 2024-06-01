n = int(input())

while n > 0:
    number = int(input())
    if number % 2 != 0:
        exit(print(f"{number} is odd!"))
    n -= 1

print("All numbers are even.")
