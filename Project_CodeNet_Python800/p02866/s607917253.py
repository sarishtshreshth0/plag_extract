from collections import Counter
n = int(input())
a = list(map(int,input().split()))
mod = 998244353
if a[0] != 0:
  print(0)
  exit()
ans = 1
c = Counter(a)
cls = list(c.items())
cls.sort()
if cls[0][1] != 1:
  print(0)
  exit()
for i in range(1,len(cls)):
  if cls[i][0] != i:
    print(0)
    exit()
  ans = ans*cls[i-1][1]**cls[i][1]%mod
print(ans)