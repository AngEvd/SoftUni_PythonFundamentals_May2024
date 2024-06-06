def main():
    print("\n".join(word for word in input().split() if len(word) % 2 == 0))


if __name__ == '__main__':
    main()

