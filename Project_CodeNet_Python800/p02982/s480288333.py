n,d = map(int, input().split())
x = [[] for g in range(n)]
c = 0
ans = 0
for h in range(n):
  x[h] = list(map(int, input().split()))
for i in range(0,n-1):
  for j in range(i+1,n):
    for k in range(d):
      c += (x[i][k] - x[j][k])**2
    if (c**0.5).is_integer():
      ans += 1
    c = 0
print(ans)