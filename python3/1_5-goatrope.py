import math

x, y, x1, y1, x2, y2 = map(int, input().split())

min_dist = width = height = 0
if x >= x1 and x <= x2:
  min_dist = min(abs(y - y1), abs(y - y2))
elif y >= y1 and y <= y2:
  min_dist = min(abs(x - x1), abs(x - x2))
else:
  if x <= x1:
    width = x1 - x
  else:
    width = x2 - x
  if y <= y1:
    height = y1 - y
  else:
    height = y2 - y

  min_dist = math.sqrt(pow(width, 2) + pow(height, 2))

print(min_dist)
