def main():
    numbers = [int(number) for number in input().split()]

    print(f"The minimum number is {min(numbers)}")
    print(f"The maximum number is {max(numbers)}")
    print(f"The sum number is: {sum(numbers)}")


if __name__ == '__main__':
    main()
