def sum_digits(num):
  total = 0
  while num > 0:
    total += num % 10
    num //= 10
  return total

bottom = int(input())
top = int(input())
total = int(input())

for i in range(bottom, top + 1):
  if sum_digits(i) == total:
    print(i)
    break

for i in range(top, bottom - 1, -1):
  if sum_digits(i) == total:
    print(i)
    break
