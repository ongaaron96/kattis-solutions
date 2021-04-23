import heapq

num_items, min_cost = map(int, input().split())
prices = list(map(int, input().split()))
heapq.heapify(prices) # O(n)

max_num_items = 1
prev_price = heapq.heappop(prices)
for _ in range(num_items - 1):
  curr_price = heapq.heappop(prices)
  if prev_price + curr_price > min_cost:
    break
  prev_price = curr_price
  max_num_items += 1

print(max_num_items)
