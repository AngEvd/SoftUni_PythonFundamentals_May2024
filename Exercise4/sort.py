def main():
    numbers = [int(number) for number in input().split()]
    numbers.sort()
    print(numbers)


if __name__ == '__main__':
    main()