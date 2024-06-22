def main():
    targets = list(map(int, input().split()))

    while True:
        command = input()
        if command == "End":
            print(f"Shot targets: {targets.count(-1)} -> {' '.join(map(str, targets))}")
            break
        else:
            index = int(command)
            if index in range(len(targets)) and targets[index] != -1:
                shot_value = targets[index]
                targets[index] = -1

                for i in range(len(targets)):
                    if targets[i] != -1:
                        if targets[i] > shot_value:
                            targets[i] -= shot_value
                        else:
                            targets[i] += shot_value


if __name__ == '__main__':
    main()


