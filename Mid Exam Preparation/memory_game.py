def main():
    elements = input().split()
    moves = 0

    while True:
        command = input()
        if command == "end":
            break
        else:
            list_len = len(elements)
            moves += 1
            index1, index2 = command.split()
            index1 = int(index1)
            index2 = int(index2)

            if index1 == index2 or index1 not in range(list_len) or index2 not in range(list_len):
                elements.insert(list_len // 2, f"-{moves}a")
                elements.insert(list_len // 2, f"-{moves}a")
                print("Invalid input! Adding additional elements to the board")
            else:
                if elements[index1] == elements[index2]:
                    print(f"Congrats! You have found matching elements - {elements[index1]}!")
                    elements.pop(max(index1, index2))
                    elements.pop(min(index1, index2))

                else:
                    print("Try again!")

                if not elements:
                    print(f"You have won in {moves} turns!")
                    return

    print("Sorry you lose :(")
    print(" ".join(elements))


if __name__ == '__main__':
    main()
