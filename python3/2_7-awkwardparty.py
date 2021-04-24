num_guests = int(input())
languages = list(map(int, input().split()))

last_index = dict()
min_dist = num_guests
for index, lang in enumerate(languages):
  if lang in last_index:
    dist = index - last_index[lang]
    
    if dist < min_dist:
      min_dist = dist
  
  last_index[lang] = index

print(min_dist)
