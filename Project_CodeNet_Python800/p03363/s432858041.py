import numpy as np
n=int(input())
a=np.array(list(map(int,input().split())))
b=a.cumsum()
from collections import Counter
c=Counter(b)
ans=0
if 0 in c:
  ans+=c[0]
for ci in c.values():
  ans+=(ci*(ci-1))//2
print(ans)