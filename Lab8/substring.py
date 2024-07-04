sub_string = input()
string = input()

while True:
    if sub_string in string:
        string = string.replace(sub_string, "")
    else:
        break

print(string)
