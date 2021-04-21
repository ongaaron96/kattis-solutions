n = int(input())

for i in range(n):
  num_guests = int(input())
  codes = input().split()

  current_codes = set()  
  for code in codes:
    if code in current_codes:
      current_codes.remove(code)
    else:
      current_codes.add(code)
  
  odd = list(current_codes)[0]
  print(f"Case #{i + 1}: {odd}")
