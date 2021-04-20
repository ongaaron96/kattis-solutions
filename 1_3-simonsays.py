n = int(input())
simon_says_str = "Simon says "

for _ in range(n):
  line = input()
  if simon_says_str in line:
    print(line.split(simon_says_str)[1])
