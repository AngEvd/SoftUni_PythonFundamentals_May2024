def main():
    names = input().split(", ")

    sorted_list = sorted(names, key=lambda x: (-len(x), x))

    print(sorted_list)


if __name__ == '__main__':
    main()
