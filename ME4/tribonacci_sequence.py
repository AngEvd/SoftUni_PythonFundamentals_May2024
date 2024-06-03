def main():
    n = int(input())
    numbers = [1]

    for i in range(1, n):
        if i < 3:
            numbers.append(i)
        else:
            numbers.append(sum(numbers[i-3:i]))

    for number in numbers:
        print(number, end=" ")
    print()


if __name__ == '__main__':
    main()



