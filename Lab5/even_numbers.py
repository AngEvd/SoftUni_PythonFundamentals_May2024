def main():
    numbers = [int(number) for number in input().split(", ")]
    print(find_even(numbers))


def find_even(numbers):
    even_indices_list = []

    for i, number in enumerate(numbers):
        if number % 2 == 0:
            even_indices_list.append(i)
    return even_indices_list


if __name__ == '__main__':
    main()
