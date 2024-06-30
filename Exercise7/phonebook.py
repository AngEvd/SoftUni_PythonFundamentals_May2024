phone_book = {}

while True:
    input_line = input()
    if "-" in input_line:
        name, phone_number = input_line.split("-")
        if name not in phone_book:
            phone_book[name] = 0
        phone_book[name] = phone_number
    else:
        number = int(input_line)
        break

for i in range(number):
    searched_name = input()
    if searched_name in phone_book:
        print(f"{searched_name} -> {phone_book[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
