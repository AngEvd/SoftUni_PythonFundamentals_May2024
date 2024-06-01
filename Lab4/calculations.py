operators = {
        "multiply": lambda a, b: a * b,
        "divide": lambda a, b: int(a / b),
        "add": lambda a, b: a + b,
        "subtract": lambda a, b: a - b
    }


def main():
    input_operator = input()
    n1, n2 = int(input()), int(input())
    print(calculate(input_operator, n1, n2))


def calculate(operator, a, b):
    operation = operators.get(operator)
    return operation(a, b)


if __name__ == "__main__":
    main()
