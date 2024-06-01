team_a, team_b = 11, 11

sent_off = set()
terminated = False

cards = input().split(" ")
for card in cards:
    if card not in sent_off:
        if card.startswith("A"):
            team_a -= 1
        elif card.startswith("B"):
            team_b -= 1
    sent_off.add(card)
    if team_a < 7 or team_b < 7:
        terminated = True
        break

print(f"Team A - {team_a}; Team B - {team_b}")
print("Game was terminated") if terminated else None
