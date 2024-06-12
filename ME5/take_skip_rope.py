def main():
    numbers, non_numbers, take, skip = [], [], [], []
    result = []

    for char in input():
        if not char.isdigit():
            non_numbers.append(char)
        else:
            numbers.append(int(char))

    for index, number in enumerate(numbers):
        take.append(number) if index % 2 == 0 else skip.append(number)

    for take_index, skip_index in zip(take, skip):
        result.extend(non_numbers[:take_index])
        non_numbers = non_numbers[take_index + skip_index:]

    print("".join(result))


if __name__ == '__main__':
    main()

