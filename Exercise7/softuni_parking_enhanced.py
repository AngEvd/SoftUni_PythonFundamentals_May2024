class Parking:
    def __init__(self):
        self.registered_cars = {}

    def register(self, name, plate):
        if name in self.registered_cars:
            return f"ERROR: already registered with plate number {self.registered_cars[name]}"
        else:
            self.registered_cars[name] = plate
            return f"{name} registered {plate} successfully"

    def unregister(self, name):
        if name in self.registered_cars:
            self.registered_cars.pop(name)
            return f"{name} unregistered successfully"
        else:
            return f"ERROR: user {name} not found"

    def __repr__(self):
        return '\n'.join([f"{name} => {self.registered_cars[name]}" for name in self.registered_cars])


softuni_parking = Parking()

commands_number = int(input())

for i in range(commands_number):
    command_line = input().split()
    command = command_line[0]
    username = command_line[1]

    if command == "register":
        register_plate = command_line[2]
        print(softuni_parking.register(username, register_plate))

    elif command == "unregister":
        print(softuni_parking.unregister(username))

print(softuni_parking.__repr__())
