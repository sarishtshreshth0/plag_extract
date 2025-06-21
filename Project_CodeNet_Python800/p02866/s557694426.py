n=int(input())
d=list(map(int,input().split()))

mod=998244353
from collections import Counter
c=Counter(d)
if not(d[0]==0 and sorted(d)[1]!=0):
  print(0)
  exit()
d.sort()
ans=1
for i in range(1,d[-1]+1):
  if c[i]==0:
    ans*=0
  else:
    ans*=c[i-1]**c[i]
  ans%=mod
print(ans)
