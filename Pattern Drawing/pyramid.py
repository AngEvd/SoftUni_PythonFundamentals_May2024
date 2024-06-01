n = int(input())

for row in range(n):
    print((n - row - 1) * " ", end="")
    print((2 * row + 1) * "*", end="")
    print((n - row - 1) * " ")


