name = input()
prev_char = result = ''

for char in name:
  if char == prev_char:
    continue

  result += char
  prev_char = char

print(result)
