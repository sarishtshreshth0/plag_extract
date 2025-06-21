#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
import bisect
n=int(input())
l=[3,5,7]
res=set()
for i in range(3,10):
    for k in itertools.product(l,repeat=i):
        if 5 not in k or 3 not in k or 7 not in k:
            continue
        else:
            num=0
            for j in range(i):
                num+=k[j]*10**(i-j-1)
            res.add(num)
res=list(res)
res.sort()
ans=bisect.bisect_right(res,n)
print(ans)