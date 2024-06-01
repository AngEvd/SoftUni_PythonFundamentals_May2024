def main():
    number1, number2 = int(input()), int(input())
    result = factorial(number1) / factorial(number2)
    print(f"{result:.2f}")


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    main()
