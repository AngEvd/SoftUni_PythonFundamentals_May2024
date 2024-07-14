n = int(input())

for _ in range(n):
    user_input = input()

    name_start = user_input.index("@") + 1
    name_end = user_input.index("|")
    age_start = user_input.index("#") + 1
    age_end = user_input.index("*")

    name = user_input[name_start: name_end]
    age = user_input[age_start: age_end]


    print(f"{name} is {age} years old.")
