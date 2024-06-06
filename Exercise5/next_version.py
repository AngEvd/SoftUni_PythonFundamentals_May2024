def main():
    version = [int(number) for number in input().split(".")]
    print(".".join(map(str, update_version(version))))


def update_version(version):
    version[-1] += 1
    for i in range(len(version) - 1, -1, -1):
        if version[i] == 10:
            version[i] = 0
            version[i - 1] += 1
    return version


if __name__ == '__main__':
    main()
