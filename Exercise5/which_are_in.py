def main():
    first_string = input().split(", ")
    second_string = input().split(", ")

    print(list(looked_word for looked_word in first_string if any(looked_word in word for word in second_string)))


if __name__ == '__main__':
    main()
