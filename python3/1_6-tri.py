def isValidEquation(var_one, var_two, result, op):
  if eval(f"{var_one}{op}{var_two}") == int(result):
    return True
  return False

nums = input().split()
operators = ['+', '-', '*', '/']

for op in operators:
  if isValidEquation(nums[0], nums[1], nums[2], op):
    print(f"{nums[0]}{op}{nums[1]}={nums[2]}")
    break

  if isValidEquation(nums[1], nums[2], nums[0], op):
    print(f"{nums[0]}={nums[1]}{op}{nums[2]}")
    break
