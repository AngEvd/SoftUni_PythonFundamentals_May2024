def main():
    rows_number = int(input())

    ship, attacked = [], []

    for i in range(rows_number):
        ship.append([int(number) for number in input().split()])

    attacked = [tuple(map(int, pair.split("-"))) for pair in input().split()]

    print(attack(ship, attacked))


def attack(ship: list, attacked: list) -> int:
    destroyed = 0
    for pair in attacked:
        row, col = pair
        if ship[row][col] > 0:
            ship[row][col] -= 1
            if ship[row][col] == 0:
                destroyed += 1
    return destroyed


if __name__ == '__main__':
    main()

