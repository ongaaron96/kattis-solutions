n = int(input())

total = 0
for _ in range(n):
  num = int(input())
  total += pow(num // 10, num % 10)

print(total)
