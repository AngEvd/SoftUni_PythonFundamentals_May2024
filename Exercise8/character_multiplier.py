from itertools import zip_longest

string1, string2 = input().split()

total_sum = 0

for char1, char2 in zip_longest(string1, string2):
    if char1 and char2:
        total_sum += ord(char1) * ord(char2)
    elif char1:
        total_sum += ord(char1)
    else:
        total_sum += ord(char2)

print(total_sum)

