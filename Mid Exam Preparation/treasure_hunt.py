def main():
    chest = input().split("|")
    average_gain = 0

    commands = {
            "Loot": loot,
            "Drop": drop,
            "Steal": steal,
    }
    while True:
        tokens = input().split()
        command = tokens[0]
        arguments = tokens[1:]

        if command == "Yohoho!":
            break
        else:
            if command in commands:
                chest = commands[command](chest, arguments)

    if chest:
        average_gain = sum(len(item) for item in chest) / len(chest)
        print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
    else:
        print("Failed treasure hunt.")


def loot(treasure: list, items: list) -> list:
    [treasure.insert(0, item) for item in items if item not in treasure]
    return treasure


def drop(treasure: list, index: list) -> list:
    index = int(index[0])
    if 0 <= index < len(treasure):
        treasure.append(treasure.pop(index))
    return treasure


def steal(treasure: list, count: list) -> list:
    count = int(count[0])
    stolen_items = treasure[-count:]
    del treasure[-count:]
    print(", ".join(stolen_items))
    return treasure


if __name__ == '__main__':
    main()
