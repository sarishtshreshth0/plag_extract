n=int(input())
a=[0]+list(map(int,input().split()))
from itertools import accumulate
a=accumulate(a)
a=list(a)
a.sort()
from collections import Counter
c=Counter(a)
ans=0
for k,v in c.items():
    if v>=2:
        ans+=v*(v-1)//2
print(ans)
