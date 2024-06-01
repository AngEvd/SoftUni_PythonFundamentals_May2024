while True:
    string = input()
    if string == "End":
        break
    elif string == "SoftUni":
        continue
    else:
        for char in string:
            print(2 * char, end="")
        print()
