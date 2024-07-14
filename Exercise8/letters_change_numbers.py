import string

words = input().split()

total = 0

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase

for word in words:
    first_letter = word[0]
    number = int(word[1:-1])
    second_letter = word[-1]

    if first_letter.isupper():
        number /= upper_letters.index(first_letter) + 1
    else:
        number *= lower_letters.index(first_letter) + 1

    if second_letter.isupper():
        number -= upper_letters.index(second_letter) + 1
    else:
        number += lower_letters.index(second_letter) + 1

    total += number

print(f"{total:.2f}")

