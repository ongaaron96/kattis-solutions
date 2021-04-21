cards_count = {'T': 0, 'C': 0, 'G': 0}

cards = input()
for c in cards:
  cards_count[c] += 1

total = 0
min_count = cards_count['T']
for count in cards_count.values():
  total += pow(count, 2)

  if count < min_count:
    min_count = count

total += min_count * 7
print(total)
