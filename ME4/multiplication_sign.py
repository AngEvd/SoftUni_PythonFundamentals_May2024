def main():
    negative = 0
    for i in range(3):
        n = int(input())
        if n == 0:
            exit(print("zero"))
        elif n < 0:
            negative += 1

    print("positive" if negative % 2 == 0 else "negative")


if __name__ == '__main__':
    main()
