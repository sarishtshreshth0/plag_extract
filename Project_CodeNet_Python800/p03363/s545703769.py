from itertools import *
from collections import *
n=int(input())
a=list(map(int,input().split()))
a=[0]+list(accumulate(a))
d=dict(Counter(a))
ans=0
for i in d.values():
  ans+=i*(i-1)//2
print(ans)