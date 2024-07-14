decrypted = input()

encrypted = ""

for char in decrypted:
    char = chr(ord(char) + 3)
    encrypted += char

print(encrypted)
