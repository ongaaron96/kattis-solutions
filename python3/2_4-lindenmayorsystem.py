num_rules, iterations = map(int, input().split())

rules = dict()
for _ in range(num_rules):
  x, _, y = input().split()
  rules[x] = y
word = input()

for _ in range(iterations):
  new_word = ""
  for char in word:
    if char in rules:
      new_word += rules[char]
    else:
      new_word += char
  word = new_word

print(word)
