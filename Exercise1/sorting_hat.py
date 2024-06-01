while True:
    name = input()
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    elif name == "Voldemort":
        exit(print("You must not speak of that name!"))
    else:
        name_length = len(name)
        if name_length < 5:
            print(f"{name} goes to Gryffindor.")
        elif name_length == 5:
            print(f"{name} goes to Slytherin.")
        elif name_length == 6:
            print(f"{name} goes to Ravenclaw.")
        else:
            print(f"{name} goes to Hufflepuff.")
