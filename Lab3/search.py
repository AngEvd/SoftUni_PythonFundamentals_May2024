n = int(input())
word = input()

lines, matching_lines = [], []

for _ in range(n):
    lines.append(input())

for line in lines:
    if word in line:
        matching_lines.append(line)

print(lines)
print(matching_lines)
