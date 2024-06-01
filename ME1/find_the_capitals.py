string = input()
output = []
i = 0
for ltr in string:
    if ltr.isupper():
        output.append(i)
    i += 1

print(output)
