text = input()

result = text[0]

for char in text[1:]:
    if char != result[-1]:
        result += char

print(result)