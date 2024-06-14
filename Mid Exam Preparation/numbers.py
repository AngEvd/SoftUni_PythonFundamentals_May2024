def main():
    numbers = [int(number) for number in input().split()]

    average = sum(numbers) / len(numbers)
    larger_than_average = [number for number in filter(lambda x: x > average, numbers)]
    larger_than_average.sort(reverse=True)

    if not larger_than_average:
        print("No")
    else:
        for i in range(min(5, len(larger_than_average))):
            print(f"{larger_than_average[i]}", end=" ")


if __name__ == '__main__':
    main()
