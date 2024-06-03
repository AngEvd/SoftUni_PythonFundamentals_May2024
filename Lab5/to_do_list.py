def main():

    notes = [0] * 10

    while True:
        command = input()
        if command == "End":
            break
        else:
            importance, task = command.split("-")
            notes.pop(int(importance) - 1)
            notes.insert(int(importance) - 1, task)

    print([note for note in notes if note != 0])


if __name__ == '__main__':
    main()
