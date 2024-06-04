def main():
    words = input().split()
    palindrome_word = input()
    palindrome_words = check_palindrome(words)
    print(palindrome_words)
    print(f"Found palindrome {palindrome_words.count(palindrome_word)} times")


def check_palindrome(string):
    palindrome_words = []
    for word in string:
        if word == "".join(reversed(word)):
            palindrome_words.append(word)

    return palindrome_words


if __name__ == '__main__':
    main()
