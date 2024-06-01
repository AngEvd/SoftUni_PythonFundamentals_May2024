def main():
    n1, n2, n3 = int(input()), int(input()), int(input())
    print(add_and_subtract(n1, n2, n3))


def sum_numbers(x, y):
    return x + y


def subtract(x, y):
    return x - y


def add_and_subtract(x, y, z):
    return subtract(sum_numbers(x, y), z)


if __name__ == "__main__":
    main()
