events = input().split("|")

energy, coins = 100, 100

for event in events:
    ingredient, number = event.split("-")
    number = int(number)

    if ingredient == "rest":
        if number + energy > 100:
            gained_energy = 100 - energy
            energy = 100

        else:
            energy += number
            gained_energy = number
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif ingredient == "order":
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")

        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= number:
            coins -= number
            print(f"You bought {ingredient}.")

        else:
            exit(print(f"Closed! Cannot afford {ingredient}."))

print("Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {energy}")
