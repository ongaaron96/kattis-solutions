input()
temps = map(int, input().split())
num_smaller_zero = sum(map(lambda x: x < 0, temps))
print(num_smaller_zero)
