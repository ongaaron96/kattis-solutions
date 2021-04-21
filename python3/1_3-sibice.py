import math

n, w, h = map(int, input().split(' '))
hypotenuse = math.sqrt(pow(w, 2) + pow(h, 2))

for _ in range(n):
  length = int(input())
  if length <= hypotenuse:
    print("DA")
  else:
    print("NE")
