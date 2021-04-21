hour, minute = map(int, input().split())
minute -= 45
if minute < 0:
  minute += 60
  hour -= 1

  if hour == -1:
    hour = 23

print(f"{hour} {minute}")
