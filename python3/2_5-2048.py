def rotate_left(matrix, n):
  return [[row[n-i-1] for row in puzzle] for i in range(n)]

def squash_left(matrix, n):
  for row in matrix:
    squashed_indexes = set()
    for curr in range(1, n):
      curr_val = row[curr]
      if curr_val == 0:
        continue

      earliest_zero_index = -1
      squashed = False
      # check previous values backwards if can squash
      for prev in range(curr-1, -1, -1):
        prev_val = row[prev]

        if prev_val == 0:
          earliest_zero_index = prev
          continue
        
        if prev not in squashed_indexes and prev_val == curr_val:
          # squash equal values
          row[prev] *= 2
          row[curr] = 0
          squashed = True
          squashed_indexes.add(prev)
        
        # prev_val != curr_val or value is squashed
        break
        
      if not squashed and earliest_zero_index >= 0:
        # push to earliest 0 slot
        row[earliest_zero_index] = curr_val
        row[curr] = 0

puzzle = []
for _ in range(4):
  puzzle.append(list(map(int, input().split())))
direction = int(input())

for _ in range(direction):
  puzzle = rotate_left(puzzle, 4)

squash_left(puzzle, 4)

if direction > 0:
  for _ in range(4 - direction):
    puzzle = rotate_left(puzzle, 4)

for row in puzzle:
  print(' '.join(map(str, row)))
