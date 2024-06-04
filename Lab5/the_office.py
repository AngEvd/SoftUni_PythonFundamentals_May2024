def main():
    happiness = [int(number) for number in input().split()]
    improvement_factor = int(input())

    happiness = list(map(lambda x: x * improvement_factor, happiness))  # improve by factor
    filtered = list(filter(lambda x: x >= sum(happiness) / len(happiness), happiness))

    happy_count = len(filtered)
    total_count = len(happiness)

    if happy_count >= total_count / 2:
        print(f"Score: {happy_count}/{total_count}. Employees are happy!")
    else:
        print(f"Score: {happy_count}/{total_count}. Employees are not happy!")


if __name__ == '__main__':
    main()

