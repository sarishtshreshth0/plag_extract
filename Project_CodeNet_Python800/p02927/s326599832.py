M, D = map(int, input().split())
ans = 0
for m in range(4, M+1):
  for d in range(22, D+1):
    if d%10 < 2:
      continue
    if m == (d//10)*(d%10):
      ans += 1
print(ans)
