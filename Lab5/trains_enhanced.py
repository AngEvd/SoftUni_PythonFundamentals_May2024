def main():
    train = [0] * int(input())

    commands = {
        "add": add,
        "insert": insert,
        "leave": leave
    }

    while True:
        command, *args = input().split()
        if command == "End":
            break
        elif command in commands:
            commands[command](train, *args)

    print(train)


def add(train, people):
    train[-1] += int(people)


def insert(train, index, people):
    train[int(index)] += int(people)


def leave(train, index, people):
    train[int(index)] -= int(people)


if __name__ == '__main__':
    main()