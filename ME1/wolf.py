user_input = input().split(", ")
wolf_index = user_input.index("wolf")

if wolf_index == len(user_input) - 1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {len(user_input) - wolf_index - 1}!"
          f" You are about to be eaten by a wolf!")
