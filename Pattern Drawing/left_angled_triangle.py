n = int(input())

for row in range(n, 0, -1):
    for col in range(row):
        print("*", end="")
    print()
