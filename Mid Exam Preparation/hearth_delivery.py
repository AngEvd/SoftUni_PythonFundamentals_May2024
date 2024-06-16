def main():
    neighbourhood = list(map(int, input().split("@")))

    current_index = 0
    while True:
        command = input()
        if command == "Love!":
            break
        jump, length = command.split()
        current_index += int(length)
        if current_index > len(neighbourhood) - 1:
            current_index = 0
        if neighbourhood[current_index] <= 0:
            print(f"Place {current_index} already had Valentine's day.")
        else:
            neighbourhood[current_index] -= 2
            if neighbourhood[current_index] <= 0:
                print(f"Place {current_index} has Valentine's day.")

    print(f"Cupid's last position was {current_index}.")

    if max(neighbourhood) <= 0:
        print(f"Mission was successful.")
    else:
        failed = list(filter(lambda x: x > 0, neighbourhood))
        print(f"Cupid has failed {len(failed)} places.")


if __name__ == '__main__':
    main()


