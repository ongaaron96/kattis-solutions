def is_periodic(word, k):
  if len(word) % k != 0:
    return False

  prev_sub = word[0:k]
  for start in range(k, len(word), k):
    curr_sub = word[start:start + k]
    if (prev_sub[-1] + prev_sub[:-1]) != curr_sub:
      return False

    prev_sub = curr_sub

  return True

word = input()
k = len(word)
for i in range(1, (len(word) // 2) + 1):
  if is_periodic(word, i):
    k = i
    break

print(k)
