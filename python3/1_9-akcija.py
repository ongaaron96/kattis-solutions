num_books = int(input())
prices = []
for _ in range(num_books):
  prices.append(int(input()))

prices.sort(reverse=True)
total_price = 0
for index, price in enumerate(prices):
  if (index + 1) % 3 == 0:
    continue
  total_price += price

print(total_price)
