class Point:
  def __init__(self, x, y, index):
    self.x = x
    self.y = y
    self.index = index
  
  def dist_to(self, other):
    return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5

def calc_total_dist(points):
  total_dist = 0
  for i in range(len(points)-1):
    total_dist += points[i].dist_to(points[i+1])
  return total_dist

def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def next_order(points):
  for i in range(len(points)-2, -1, -1):
    # 1. Find largest i such that P[i] < P[i+1]
    if points[i].index < points[i+1].index:
      # 2. Find largest j such that P[i] < P[j]
      for j in range(len(points)-1, -1, -1):
        if points[i].index < points[j].index:
          # 3. Swap P[i] and P[j]
          swap(points, i, j)
          # 4. Reverse P[i+1 .. n]
          right_arr = points[i+1:]
          right_arr.reverse()
          return points[:i+1] + right_arr
  return None

num_points = int(input())
points = []
for i in range(num_points):
  x, y = map(float, input().split())
  points.append(Point(x, y, i))

orders_done = set()
best_dist = -1
best_order = []
while not points is None:
  reverse_order = ''.join([str(p.index) for p in points[::-1]])
  if reverse_order not in orders_done:  
    # print(' '.join([str(p.index) for p in points]))
    total_dist = calc_total_dist(points)
    if best_dist == -1 or total_dist < best_dist:
      best_dist = total_dist
      best_order = points.copy()
      # print(best_dist)
    orders_done.add(''.join([str(p.index) for p in points]))

  points = next_order(points)

for point in best_order:
  print(point.index)
