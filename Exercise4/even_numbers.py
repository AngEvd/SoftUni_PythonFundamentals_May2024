def main():
    numbers = [int(number) for number in input().split()]
    print(list(filter(even, numbers)))


def even(n):
    return n % 2 == 0


if __name__ == '__main__':
    main()
