def main():

    train = [0] * int(input())

    while True:
        command = input()
        if command == "End":
            break
        elif command.startswith("add"):
            command_name, people = command.split()
            train[-1] += int(people)
        else:
            command_name, index, people = command.split()

            if command_name == "insert":
                train[int(index)] += int(people)
            else:
                train[int(index)] -= int(people)

    print(train)


if __name__ == '__main__':
    main()
