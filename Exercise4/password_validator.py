def main():
    password_validator(input())


def password_validator(password):
    digits = 0
    valid = True
    if not 6 <= len(password) <= 10:
        valid = False
        print("Password must be between 6 and 10 characters")
    for char in password:
        if ord(char) not in range(48, 57+1) and ord(char) not in range(65, 90+1) and ord(char) not in range(97, 122+1):
            valid = False
            print("Password must consist only of letters and digits")
            break
        if ord(char) in range(48, 57+1):
            digits += 1
    if digits < 2:
        valid = False
        print("Password must have at least 2 digits")
    if valid:
        print("Password is valid")


if __name__ == '__main__':
    main()
