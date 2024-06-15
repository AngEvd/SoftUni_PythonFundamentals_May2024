def main():
    chest = input().split(", ")

    commands = {
        "Collect": lambda: collect(chest, item),
        "Drop": lambda: drop(chest, item),
        "Combine Items": lambda: combine(chest, item),
        "Renew": lambda: renew(chest, item),
    }

    while True:
        action = input()

        if action == "Craft!":
            break
        else:
            command, item = action.split(" - ")
            commands[command]()

    print(", ".join(chest))


def collect(chest: list, item: str) -> list:
    if item not in chest:
        chest.append(item)
    return chest


def drop(chest: list, item: str) -> list:
    if item in chest:
        chest.remove(item)
    return chest


def combine(chest: list, item: str) -> list:
    old_tem, new_item = item.split(":")
    if old_tem in chest:
        chest.insert(chest.index(old_tem) + 1, new_item)
    return chest


def renew(chest: list, item: str) -> list:
    if item in chest:
        chest.remove(item)
        chest.append(item)
    return chest


if __name__ == '__main__':
    main()
