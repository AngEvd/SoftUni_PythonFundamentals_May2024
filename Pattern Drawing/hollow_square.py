number = int(input())

for i in range(number):
    if i == 0 or i == number - 1:
        print(number * "*")
    else:
        print("*" + (number - 2) * " " + "*")
