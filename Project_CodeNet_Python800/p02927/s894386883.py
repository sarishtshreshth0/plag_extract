M, D = map(int, input().split())

c = 0
for m in range(1, M+1):
  for d in range(1, D+1):
    d10 = d//10
    d1 = d - (d//10 * 10)
    # print(m, d10, d1)
    if d10 * d1 == m:
      if d1 >= 2 and d10 >= 2:
        c += 1
        # print(m, d)

print(c)