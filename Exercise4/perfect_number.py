def main():
    number = int(input())
    print("We have a perfect number!" if is_perfect(number) else "It's not so perfect.")


def is_perfect(number):
    dividers_sum = 0
    for i in range(1, number):
        if number % i == 0:
            dividers_sum += i
    return number == dividers_sum


if __name__ == '__main__':
    main()
