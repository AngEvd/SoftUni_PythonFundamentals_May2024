def main():
    pirate_ship = list(map(int, input().split(">")))
    man_o_war = list(map(int, input().split(">")))
    max_health_capacity = int(input())

    while True:
        command_line = input().split()
        command = command_line[0]
        arguments = command_line[1:]

        commands = {
            "Fire": lambda: fire(man_o_war, arguments),
            "Defend": lambda: defend(pirate_ship, arguments),
            "Repair": lambda: repair(pirate_ship, arguments, max_health_capacity),
            "Status": lambda: status(pirate_ship, max_health_capacity),
        }

        if command == "Retire":
            print(f"Pirate ship status: {sum(pirate_ship)}")
            print(f"Warship status: {sum(man_o_war)}")
            break
        else:
            commands[command]()


def fire(ship: list, arguments: list) -> list:
    index, damage = map(int, arguments)
    if 0 <= index < len(ship):
        ship[index] -= damage
        if ship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            exit()
    return ship


def defend(ship: list, arguments: list) -> list:
    start_index, end_index, damage = map(int, arguments)
    if 0 <= start_index < len(ship) and start_index <= end_index < len(ship):
        for i in range(start_index, end_index + 1):
            ship[i] -= damage
            if ship[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()
    return ship


def repair(ship: list, arguments: list, max_health: int) -> list:
    index, health = map(int, arguments)
    if 0 <= index < len(ship):
        ship[index] = min(ship[index] + health, max_health)
    return ship


def status(ship: list, max_health: int) -> None:
    sections_to_repair = [section for section in ship if section < 0.2 * max_health]
    print(f"{len(sections_to_repair)} sections need repair.")


if __name__ == '__main__':
    main()
