numbers = input().split(", ")
beggars = int(input())

loot = [0] * beggars
beggar_turn = 0

for number in numbers:
    loot[beggar_turn] += int(number)
    beggar_turn = (beggar_turn + 1) % beggars

print(loot)
