n = int(input())

qaly = 0
for _ in range(n):
  q, y = map(float, input().split())
  qaly += q*y

print(qaly)
