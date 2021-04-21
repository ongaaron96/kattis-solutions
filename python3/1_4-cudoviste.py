def compute_cars_squashed(matrix, row, col):
  cars_squashed = 0
  for r in range(row, row + 2):
    for c in range(col, col + 2):
      char = matrix[r][c]

      if char == '#':
        return -1
      
      if char == 'X':
        cars_squashed += 1

  return cars_squashed


rows, cols = map(int, input().split())
carpark = ['' for _ in range(rows)]

for i in range(rows):
  carpark[i] = input()

results = [0] * 5
for r in range(rows - 1):
  for c in range(cols - 1):
    cars_squashed = compute_cars_squashed(carpark, r, c)

    if cars_squashed != -1:
      results[cars_squashed] += 1
    
for res in results:
  print(res)
