moves = [input().split(),
         input().split(),
         input().split()]

result = {"0": "Draw!", "1": "First player won", "2": "Second player won"}

if moves[0][0] == moves[0][1] == moves[0][2]:
    winner = moves[0][0]
elif moves[1][0] == moves[1][1] == moves[1][2]:
    winner = moves[1][0]
elif moves[2][0] == moves[2][1] == moves[2][2]:
    winner = moves[2][0]
elif moves[0][0] == moves[1][0] == moves[2][0]:
    winner = moves[0][0]
elif moves[0][1] == moves[1][1] == moves[2][1]:
    winner = moves[0][1]
elif moves[0][2] == moves[1][2] == moves[2][2]:
    winner = moves[0][0]
elif moves[0][0] == moves[1][1] == moves[2][2]:
    winner = moves[0][0]
elif moves[0][2] == moves[1][1] == moves[2][0]:
    winner = moves[0][2]
else:
    winner = "0"

print(result.get(winner))
