def main():
    char1, char2 = input(), input()
    print(char_in_range(char1, char2))


def char_in_range(a, b):
    string = ""
    for i in range(ord(a) + 1, ord(b)):
        string += " " + chr(i)
    return string.strip()


if __name__ == '__main__':
    main()
