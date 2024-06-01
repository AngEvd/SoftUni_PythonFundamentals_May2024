number = int(input())

for _ in range(number):
    string = input()
    if any(char in string for char in ".,_"):
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
