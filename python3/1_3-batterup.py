n = int(input())
points = map(int, input().split())
total_points = 0

for point in points:
  if point == -1:
    n -= 1
    continue

  total_points += point

print(total_points / n)
