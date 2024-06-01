gifts = input().split(" ")
result = ""

while True:
    command = input()
    if command == "No Money":
        break

    arguments = command.split(" ")

    action = arguments[0]
    gift_name = arguments[1]

    if action == "OutOfStock":
        gifts = ["None" if gift == gift_name else gift for gift in gifts]
    elif action == "Required" and len(arguments) == 3:
        gift_index = int(arguments[2])
        if 0 <= gift_index < len(gifts):
            gifts[gift_index] = gift_name
    else:
        gifts[-1] = gift_name

print(" ".join(gift for gift in gifts if gift is not None and gift != "None"))
