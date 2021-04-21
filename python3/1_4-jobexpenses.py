input()
nums = map(int, input().split())

expenses = 0
for num in nums:
  if num < 0:
    expenses += -num

print(expenses)
