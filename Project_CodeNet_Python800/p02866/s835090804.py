from collections import Counter

N=int(input())
*d,=map(int,input().split())
mod = 998244353

if d[0]:
  print(0)
  exit()
  
dmax = max(d)
if sorted(set(d)) != list(range(dmax+1)):
  print(0)
  exit()

c = Counter(d)

if c[0]>1:
  print(0)
  exit()

ans =1
for i in range(2,dmax+1):
  ans *= pow(c[i-1],c[i],mod)
  ans %= mod
  
print(ans)