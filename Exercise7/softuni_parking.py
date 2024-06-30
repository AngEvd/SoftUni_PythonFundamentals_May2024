registered_cars = {}
commands_number = int(input())

for i in range(commands_number):
    command_line = input().split()
    command = command_line[0]
    username = command_line[1]
    if command == "register":
        register_plate = command_line[2]
        if username in registered_cars:
            print(f"ERROR: already registered with plate number {registered_cars[username]}")
        else:
            registered_cars[username] = register_plate
            print(f"{username} registered {register_plate} successfully")
    elif command == "unregister":
        if username in registered_cars:
            registered_cars.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for username in registered_cars:
    print(f"{username} => {registered_cars[username]}")


