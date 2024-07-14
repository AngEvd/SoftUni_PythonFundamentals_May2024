import itertools

keys = list(map(int, input().split()))

while True:
    user_input = input()
    decrypted_message = ""
    if user_input == "find":
        break

    for char, key in zip(user_input, itertools.cycle(keys)):
        decrypted_message += (chr(ord(char) - key))

    treasure = decrypted_message.split("&")[1]

    coordinates_start = decrypted_message.find("<") + 1
    coordinates_end = decrypted_message.find(">")

    coordinates = decrypted_message[coordinates_start: coordinates_end]

    print(f"Found {treasure} at {coordinates}")
