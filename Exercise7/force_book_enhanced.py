class Book:
    def __init__(self):
        self.book = {}

    def add_user(self, side, user):
        if all(user not in users for users in self.book.values()):
            if side not in self.book:
                self.book[side] = []
            self.book[side].append(user)

    def switch_sides(self, side, user):
        for key in self.book:
            if user in self.book[key]:
                self.book[key].remove(user)

        if side not in self.book.keys():
            self.book[side] = []
        self.book[side].append(user)
        return f"{user} joins the {side} side!"

    def __repr__(self):
        book_repr = []
        for force, members in self.book.items():
            if len(members) > 0:
                book_repr.append(f"Side: {force}, Members: {len(members)}")
                for member in members:
                    book_repr.append(f"! {member}")
        return "\n".join(book_repr)


force_book = Book()

while True:
    command_line = input()
    if command_line == "Lumpawaroo":
        break

    if "|" in command_line:
        force_side, force_user = command_line.split(" | ")
        force_book.add_user(force_side, force_user)

    elif "->" in command_line:
        force_user, force_side = command_line.split(" -> ")
        print(force_book.switch_sides(force_side, force_user))

print(force_book.__repr__())
