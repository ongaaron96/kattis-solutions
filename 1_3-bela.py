values = {'A': [11, 11], 'K': [4, 4], 'Q': [3, 3], 'J': [20, 2], 'T': [10, 10], '9': [14, 0], '8': [0, 0], '7': [0, 0]}
n, dom_suit = input().split()
points = 0

for _ in range(4 * int(n)):
  card = input()
  
  if card[1] == dom_suit:
    points += values[card[0]][0]
  else:
    points += values[card[0]][1]

print(points)
