def swap(arr, first, second):
  temp = arr[first]
  arr[first] = arr[second]
  arr[second] = temp

moves = input()
arr = [1, 0, 0]
for c in moves:
  if c == 'A':
    swap(arr, 0, 1)
  elif c == 'B':
    swap(arr, 1, 2)
  else:
    swap(arr, 0, 2)

for index, val in enumerate(arr):
  if val == 1:
    print(index + 1)
    break
