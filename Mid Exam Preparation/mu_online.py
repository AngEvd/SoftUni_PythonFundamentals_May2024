def main():
    dungeon = input().split("|")
    bitcoin, health = check_room(dungeon)
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")


def check_room(dungeon: list, health=100, bitcoin=0) -> tuple:
    room_number = 1
    for room in dungeon:
        command, number = room.split()
        number = int(number)

        if command == "potion":
            print(f"You healed for {min(100 - health, number)} hp.")
            health = min(health + number, 100)
            print(f"Current health: {health} hp.")
        elif command == "chest":
            bitcoin += number
            print(f"You found {number} bitcoins.")
        else:
            health -= number
            if health > 0:
                print(f"You slayed {command}.")
            else:
                print(f"You died! Killed by {command}.")
                print(f"Best room: {room_number}")
                exit()

        room_number += 1

    return bitcoin, health


if __name__ == '__main__':
    main()
