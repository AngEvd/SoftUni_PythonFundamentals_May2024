def main():
    numbers = [int(number) for number in input().split(", ")]

    max_number = max(numbers)
    max_group = max_number // 10 * 10 if max_number % 10 == 0 else max_number // 10 * 10 + 10
    for n in range(0, max_group, 10):
        print(f"Group of {n + 10}'s: {list(number for number in numbers if n < number <= n + 10)}")


if __name__ == '__main__':
    main()


