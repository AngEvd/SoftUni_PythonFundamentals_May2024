def main():
    command, user_input = input(), input()

    commands = {
        "int": modify_int,
        "real": modify_float,
        "string": modify_string
    }

    print((commands.get(command))(user_input))


def modify_int(number):
    return int(number) * 2


def modify_float(number):
    return f"{float(number) * 1.5:.2f}"


def modify_string(text):
    return f"${text}$"


if __name__ == '__main__':
    main()
