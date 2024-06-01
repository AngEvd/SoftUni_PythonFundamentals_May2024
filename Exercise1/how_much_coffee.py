events = ["coding", "dog", "cat", "movie"]

coffees = 0

while True:
    command = input()
    if command == "END":
        break
    elif command.casefold() not in events:
        continue
    else:
        if command.islower():
            coffees += 1
        else:
            coffees += 2

print("You need extra sleep") if coffees > 5 else print(coffees)
