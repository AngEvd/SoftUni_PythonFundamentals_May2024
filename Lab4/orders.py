prices = {
    "coffee": 1.50,
    "water": 1.00,
    "coke": 1.40,
    "snacks": 2.0
}


def main():
    product = input()
    qty = int(input())

    print(calculate(product, qty))


def calculate(product, quantity):
    return f"{prices.get(product) * quantity:.2f}"


if __name__ == "__main__":
    main()
