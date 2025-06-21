M, D = [int(_) for _ in input().split()]
ans = 0
for m in range(1, M+1):
  for d in range(1, D+1):
    d0 = d%10
    d10 = (d - d%10)//10
    if d0 > 1 and d10 > 1 and d0 * d10 == m: ans += 1
print(ans)

