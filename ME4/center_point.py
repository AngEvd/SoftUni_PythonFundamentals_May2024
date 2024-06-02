import math


def main():
    x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
    print(check_coordinates(x1, y1, x2, y2))


def check_coordinates(a, b, c, d):
    radius1 = math.sqrt(pow(a, 2) + pow(b, 2))
    radius2 = math.sqrt(pow(c, 2) + pow(d, 2))
    if radius1 <= radius2:
        return math.floor(a), math.floor(b)
    else:
        return math.floor(c), math.floor(d)


if __name__ == '__main__':
    main()
