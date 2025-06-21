from scipy.special import comb
from collections import Counter as C
n=int(input())
a=list(map(int,input().split()))

l=[0]*(n+1)
tmp=0
for i in range(0,n):
  l[i+1]=tmp+a[i]
  tmp=l[i+1]

c=C(l)
ans=0

for v in c.values():
  ans+=comb(v, 2, exact=True)
print(ans)