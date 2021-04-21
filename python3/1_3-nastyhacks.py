n = int(input())

for _ in range(n):
  rev_no_adv, rev_adv, cost = map(int, input().split())
  profit_adv = rev_adv - cost

  if rev_no_adv > profit_adv:
    print("do not advertise")
  elif rev_no_adv == profit_adv:
    print("does not matter")
  else:
    print("advertise")
