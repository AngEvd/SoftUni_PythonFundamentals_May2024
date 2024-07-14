text = input()

result = ""
explosion = 0
index = 0

for char in text:
    if char == ">":
        explosion += int(text[index+1])
        result += char
    elif explosion > 0:
        explosion -= 1
    else:
        result += char
    index += 1

print(result)
