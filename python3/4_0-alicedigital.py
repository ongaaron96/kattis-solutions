num_datasets = int(input())
for _ in range(num_datasets):
  _, min_val = map(int, input().split())
  values = map(int, input().split())

  curr_sum = next_sum = max_sum = 0
  min_val_passed = False
  for val in values:
    if val < min_val:
      if min_val_passed:
        max_sum = max(curr_sum, max_sum)
        min_val_passed = False
      curr_sum = next_sum = 0
    elif val == min_val:
      min_val_passed = True
      max_sum = max(curr_sum, max_sum)
      curr_sum = next_sum + val
      next_sum = 0
    else:
      curr_sum += val
      next_sum += val

  if min_val_passed:
    max_sum = max(curr_sum, max_sum)
  print(max_sum)
