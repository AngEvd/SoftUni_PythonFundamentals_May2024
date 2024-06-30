string = input()
chars = {}

for char in string:
    if char != " ":
        if char not in chars:
            chars[char] = 0
        chars[char] += 1

for char in chars:
    print(f"{char} -> {chars[char]}")
