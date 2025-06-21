M,D = list(map(int, input().split()))

ans = 0
for m in range(1,M+1):
  for d in range(2,D+1):
    if d // 10 < 2 or d % 10 < 2:
      continue
    if (d//10) * (d%10) == m:
      ans += 1
      
print(ans)