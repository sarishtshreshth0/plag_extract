#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
from fractions  import gcd
#input=sys.stdin.readline
#import bisect

n,m=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(n)]
d=[]
ab=sorted(ab,key=lambda x: x[0])
ans=0
j=0
for i in range(m):
    for k in range(j,n):
        if ab[k][0]>i+1:
            j=k
            break
        heapq.heappush(d,(-1)*ab[k][1])
    else:
      j=n
    if not d:
        continue
    res=heapq.heappop(d)*(-1)
    ans+=res
    
print(ans)