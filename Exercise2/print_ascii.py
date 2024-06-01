start, end = int(input()), int(input())

string = ""

for char in range(start, end + 1):
    string += chr(char) + " "

print(string.strip())
