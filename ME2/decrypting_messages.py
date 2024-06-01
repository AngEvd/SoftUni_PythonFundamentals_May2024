key = int(input())
lines = int(input())

decrypted_string = ""

for line in range(lines):
    encrypted_char = ord(input())
    decrypted_string += chr(encrypted_char + key)

print(decrypted_string)
