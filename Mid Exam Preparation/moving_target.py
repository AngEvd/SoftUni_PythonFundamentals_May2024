def main():
    targets = list(map(int, input().split()))

    commands = {
        "Shoot": lambda: shoot(int(value1), int(value2), targets),
        "Add": lambda: add(int(value1), int(value2), targets),
        "Strike": lambda: strike(int(value1), int(value2), targets)
    }

    while True:
        command = input()

        if command == "End":
            print("|".join(map(str, targets)))
            break
        else:
            command, value1, value2 = command.split()
            commands[command]()


def shoot(index: int, power: int, targets: list) -> list:
    if index in range(len(targets)):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
    return targets


def add(index: int, value: int, targets: list) -> list:
    if index in range(len(targets)):
        targets.insert(index, value)
    else:
        print("Invalid placement!")
    return targets


def strike(index: int, radius: int, targets: list) -> list:
    if 0 <= (index - radius) < len(targets) and 0 <= (index + radius) < len(targets):
        for i in range(index + radius, index - radius - 1, -1):
            targets.pop(i)
    else:
        print("Strike missed!")
    return targets


if __name__ == '__main__':
    main()
