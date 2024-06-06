def main():
    electron_numbers = int(input())
    print(fill_shell(electron_numbers))


def fill_shell(electrons):
    shell = []
    shell_number = 1

    while electrons > 0:
        max_electrons = 2 * pow(shell_number, 2)
        shell.append(min(electrons, max_electrons))
        electrons -= max_electrons
        shell_number += 1

    return shell


if __name__ == '__main__':
    main()
