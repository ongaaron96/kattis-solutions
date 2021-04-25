class Point:
  def __init__(self, x, y, index):
    self.x = x
    self.y = y
    self.index = index

def distance(point, other):
  return ((point.x - other.x)**2 + (point.y - other.y)**2) ** 0.5

num_points = int(input())
points = []
for i in range(num_points):
  x, y = map(float, input().split())
  points.append(Point(x, y, i))

# order points based on how far they are from the average coordinate
mean_x = sum([p.x for p in points]) / num_points
mean_y = sum([p.y for p in points]) / num_points
mean = Point(mean_x, mean_y, -1)
points = sorted(points, key=lambda p: -distance(p, mean))
for p in points:
  print(distance(p, mean))

best_tour = []
best_dist = -1
# start at each point
for i in range(min(num_points, 40)):
  first_point = points[i]
  tour = [first_point]
  used = [False for _ in range(num_points)]
  used[first_point.index] = True
  total_dist = 0

  for j in range(1, num_points):
    closest_point = None
    closest_dist = -1

    # find closest point
    for k in range(num_points):
      if used[points[k].index]:
        continue
      if closest_point == None or distance(tour[j-1], points[k]) < closest_dist:
        closest_point = points[k]
        closest_dist = distance(tour[j-1], points[k])

    tour.append(closest_point)
    total_dist += closest_dist
    used[closest_point.index] = True

  if best_dist == -1 or total_dist < best_dist:
    best_tour = tour
    best_dist = total_dist

for point in best_tour:
  print(point.index)
