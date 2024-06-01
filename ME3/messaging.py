first_line = input().split(" ")
second_line = list(input())

indexes = []

for value in first_line:
    index_sum = 0
    for char in value:
        index_sum += int(char)
    indexes.append(index_sum)

for value in indexes:
    index = value % len(second_line)
    print(second_line.pop(index), end="")

print()
