def main():
    numbers = [int(number) for number in input().split(", ")]
    for number in numbers:
        print(check_palindrome(number))


def check_palindrome(x):
    reversed_x = 0
    temp = x
    while temp > 0:
        reversed_x = reversed_x * 10 + temp % 10
        temp //= 10
    return x == reversed_x


if __name__ == '__main__':
    main()
