max_points = -1
winner_num = -1

for i in range(5):
  points = sum(map(int, input().split()))
  if points > max_points:
    max_points = points
    winner_num = i + 1

print(f"{winner_num} {max_points}")
