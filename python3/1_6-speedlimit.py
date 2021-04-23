n = int(input())

while n != -1:
  total_dist = 0
  prev_time = 0

  for _ in range(n):
    speed, time = map(int, input().split())
    total_dist += speed * (time - prev_time)
    prev_time = time

  print(f"{total_dist} miles")
  n = int(input())
