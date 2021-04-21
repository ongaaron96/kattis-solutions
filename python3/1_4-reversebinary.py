num = int(input())
reverse_binary = ''
while num > 0:
  reverse_binary += str(num % 2)
  num //= 2

total = 0
for index, digit in enumerate(reverse_binary[::-1]):
  total += pow(2, index) * int(digit)
print(total)
