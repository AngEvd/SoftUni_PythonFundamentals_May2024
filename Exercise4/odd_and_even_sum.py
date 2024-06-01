def main():
    print(odd_even_sum(input()))


def odd_even_sum(string):
    odd_sum, even_sum = 0, 0
    for s in string:
        s = int(s)
        if s % 2 != 0:
            odd_sum += s
        else:
            even_sum += s

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


if __name__ == '__main__':
    main()
