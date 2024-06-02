from math import sqrt


def main():
    x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
    x3, y3, x4, y4 = float(input()), float(input()), float(input()), float(input())
    print(compare_lines(x1, y1, x2, y2, x3, y3, x4, y4))


def compare_lines(x1, y1, x2, y2, x3, y3, x4, y4):
    line1 = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    line2 = sqrt(pow(x3 - x4, 2) + pow(y3 - y4, 2))

    if line1 >= line2:
        if is_closer_to_center(x1, y1, x2, y2):
            return f"({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})"
        else:
            return f"({int(x2)}, {int(y2)})({int(x1)}, {int(y1)})"
    else:
        if is_closer_to_center(x3, y3, x4, y4):
            return f"({int(x3)}, {int(y3)})({int(x4)}, {int(y4)})"
        else:
            return f"({int(x4)}, {int(y4)})({int(x3)}, {int(y3)})"


def is_closer_to_center(a, b, c, d):
    radius1 = sqrt(pow(a, 2) + pow(b, 2))
    radius2 = sqrt(pow(c, 2) + pow(d, 2))
    if radius1 <= radius2:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
