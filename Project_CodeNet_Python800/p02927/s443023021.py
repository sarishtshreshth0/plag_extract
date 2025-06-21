M, D = map(int,input().split())
ans = 0
for m in range(1,M+1):
  if D<=9:continue
  for d in range(10,D+1):
    strd = str(d)
    d10, d1 = int(strd[0]), int(strd[1]) 
    if d10>=2 and d1>=2 and d1*d10==m: ans += 1
print(ans)