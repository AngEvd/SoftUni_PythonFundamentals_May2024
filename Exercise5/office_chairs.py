def main():
    room_numbers = int(input())

    room = 0
    empty_chairs = 0
    enough_chairs = True

    for i in range(room_numbers):
        chairs, visitors = input().split()
        chairs = len(chairs)
        visitors = int(visitors)
        room += 1
        if chairs < int(visitors):
            print(f"{visitors - chairs} more chairs needed in room {room}")
            enough_chairs = False
        elif chairs > visitors:
            empty_chairs += chairs - visitors

    if enough_chairs:
        print(f"Game On, {empty_chairs} free chairs left")


if __name__ == '__main__':
    main()
