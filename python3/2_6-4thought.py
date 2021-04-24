def get_expression(n):
  operations = ['+', '-', '*', '//']
  for op_one in operations:
    for op_two in operations:
      for op_three in operations:
        expression = f"4 {op_one} 4 {op_two} 4 {op_three} 4"
        if eval(expression) == n:
          return expression.replace("//", "/")
  return ""

num_cases = int(input())
for _ in range(num_cases):
  n = int(input())
  expression = get_expression(n)

  if len(expression) == 0:
    print("no solution")
  else:
    print(f"{expression} = {n}")
