def main():
    encrypted_words = input().split()
    deciphered_words = [decipher_word(word) for word in encrypted_words]
    print(" ".join(deciphered_words))


def decipher_word(word):
    first_char = ""
    i = 0
    while i < len(word) and word[i].isdigit():
        first_char += word[i]
        i += 1

    first_letter = chr(int(first_char))
    rest_of_word = word[i:]

    if len(rest_of_word) > 1:
        rest_of_word = rest_of_word[-1] + rest_of_word[1:-1] + rest_of_word[0]

    deciphered_word = first_letter + rest_of_word
    return deciphered_word


if __name__ == '__main__':
    main()
