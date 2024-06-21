def main():
    total, taxes = 0, 0
    discount = 1
    tax = 0.2

    while True:
        price = input()
        if price == "special":
            discount = 0.9
            break
        elif price == "regular":
            break
        else:
            if float(price) >= 0:
                total += float(price)
            else:
                print("Invalid price!")

    if total == 0:
        print("Invalid order!")
    else:
        taxes = total * tax

        print(f"Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {(total + taxes) * discount:.2f}$")


if __name__ == '__main__':
    main()
