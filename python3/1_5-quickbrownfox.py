n = int(input())

for _ in range(n):
  sentence = input()
  letters = set()

  for char in sentence:
    letters.add(char.lower())

  missing = ''
  for i in range(ord('a'), ord('z') + 1):
    if chr(i) not in letters:
      missing += chr(i)

  if len(missing) == 0:
    print("pangram")
  else:
    print(f"missing {missing}")
  