_, increase, sped_time = map(int, input().split())
time_stamps = list(map(int, input().split()))
time_stamps.append(sped_time)

original_time = 0
prev_time = 0
current_increase = 1.0
for time in time_stamps:
  original_time += (time - prev_time) * current_increase
  current_increase += increase / 100
  prev_time = time

print(original_time)
