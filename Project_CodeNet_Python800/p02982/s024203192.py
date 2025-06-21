import math
n, d = map(int, input().split())
a = []
ans = 0
x = 0
if d ==1:
  for i in range(n):
    a.append(int(input()))
  for i in range(n):
    for j in range(i,n):
      if math.sqrt((a[i]-a[j])**2)%1==0 and math.sqrt((a[i]-a[j])**2)!=0:
        ans += 1
else:
  for i in range(n):
    a.append(list(map(int, input().split())))
  for i in range(n):
    for j in range(i, n):
      x = 0
      for k in range(d):
        x += (a[i][k] - a[j][k]) **2
      if math.sqrt(x)%1 == 0 and math.sqrt(x) != 0:
        ans += 1
print(ans)