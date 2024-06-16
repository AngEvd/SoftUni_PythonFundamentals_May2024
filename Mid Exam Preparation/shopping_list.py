def main():
    shopping_list = input().split("!")

    commands = {
        "Urgent": lambda: add_item(shopping_list, item),
        "Unnecessary": lambda: drop_item(shopping_list, item),
        "Correct": lambda: correct_item(shopping_list, item, new_item),
        "Rearrange": lambda: rearrange_item(shopping_list, item)
    }

    while True:
        action = input()
        if "Go Shopping!" in action:
            break
        elif "Correct" in action:
            command, item, new_item = action.split()
        else:
            command, item = action.split()
        shopping_list = commands[command]()

    print(", ".join(shopping_list))


def add_item(shopping_list: list, item: str) -> list:
    if item not in shopping_list:
        shopping_list.insert(0, item)
    return shopping_list


def drop_item(shopping_list: list, item: str) -> list:
    if item in shopping_list:
        shopping_list.remove(item)
    return shopping_list


def correct_item(shopping_list: list, item: str, new_item) -> list:
    if item in shopping_list:
        index = shopping_list.index(item)
        shopping_list.pop(index)
        shopping_list.insert(index, new_item)
    return shopping_list


def rearrange_item(shopping_list: list, item: str) -> list:
    if item in shopping_list:
        shopping_list.remove(item)
        shopping_list.append(item)
    return shopping_list


if __name__ == '__main__':
    main()

