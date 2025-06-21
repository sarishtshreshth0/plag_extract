M, D = [int(i) for i in input().split()]
cnt = 0
for m in range(1, M + 1):
  for d in range(1, D + 1):
    d1 = d // 10
    d2 = d % 10
    if d1 < 2 or d2 < 2:
      continue
    if d1 * d2 == m:
      cnt += 1
print(cnt)