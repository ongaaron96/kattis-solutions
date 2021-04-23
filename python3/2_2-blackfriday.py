input()
rolls = list(map(int, input().split()))

roll_to_players = [[] for _ in range(6)]
for index, roll in enumerate(rolls):
  roll_to_players[roll - 1].append(index + 1)

winner = 0
for players in roll_to_players[::-1]:
  if len(players) == 1:
    winner = players[0]
    break

if winner == 0:
  print("none")
else:
  print(winner)
