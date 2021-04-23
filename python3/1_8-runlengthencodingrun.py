code, word = input().split()

result = ""
if code == 'E':
  prev_char = word[0]
  prev_char_count = 1

  for c in word[1:]:
    if c == prev_char:
      prev_char_count += 1
    else:
      result += prev_char + str(prev_char_count)
      prev_char = c
      prev_char_count = 1

  result += prev_char + str(prev_char_count)

else:
  for index, c in enumerate(word):
    if c.isdigit():
      result += word[index - 1] * int(c)

print(result)
