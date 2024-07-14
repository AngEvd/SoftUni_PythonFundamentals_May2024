first_char, second_char, text = input(), input(), input()

ascii_sum = 0
first_char_ascii = ord(first_char)
second_char_ascii = ord(second_char)

for char in text:
    if first_char_ascii < ord(char) < second_char_ascii:
        ascii_sum += ord(char)

print(ascii_sum)
