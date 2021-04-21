num_articles, impact = map(int, input().split())
num_scientists = num_articles * (impact - 1) + 1
print(num_scientists)
