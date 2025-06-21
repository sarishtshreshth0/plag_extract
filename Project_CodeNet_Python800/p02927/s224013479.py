m,d=map(int,input().split())
ans = 0
for i in range(1,m+1):
  for j in range(1,d+1):
    if j%10>=2 and j//10>=2 and i==j//10*(j%10): ans += 1
print(ans)