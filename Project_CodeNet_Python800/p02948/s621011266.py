n,m=map(int,input().split())
A=[]
for i in range(n):
    a,b=map(int,input().split())
    A.append([a,b])
A=sorted(A, key=lambda x:(x[0], -x[1]))
from collections import deque
A=deque(A)

# import numpy as np
import bisect as bi
ans=0
now=[]
for nouki in range(1,m+1):
    while A:
        a,b=A.popleft()
        if a>nouki: A.appendleft([a,b]);break
        bi.insort(now,b)
    #print(nouki, now)
    if now==[]:continue
    ans+= now[-1]
    del now[-1]


print(ans)
    
