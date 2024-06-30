book = {}

while True:
    command_line = input()
    if command_line == "Lumpawaroo":
        break

    if "|" in command_line:
        force_side, user = command_line.split(" | ")
        if all(user not in users for users in book.values()):
            if force_side not in book:
                book[force_side] = []
            book[force_side].append(user)

    elif "->" in command_line:
        user, force_side = command_line.split(" -> ")
        for side in book:
            if user in book[side]:
                book[side].remove(user)

        if force_side not in book.keys():
            book[force_side] = []
        book[force_side].append(user)
        print(f"{user} joins the {force_side} side!")

for force, members in book.items():
    if len(members) > 0:
        print(f"Side: {force}, Members: {len(members)}")
        for member in members:
            print(f"! {member}")
