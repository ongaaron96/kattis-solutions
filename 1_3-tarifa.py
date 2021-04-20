x = int(input())
n = int(input())

total_used = 0
for _ in range(n):
  total_used += int(input())

amount_available = (n+1) * x - total_used
print(amount_available)
