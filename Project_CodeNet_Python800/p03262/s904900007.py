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
#import bisect
n,x0=map(int,input().split())
x=list(map(int,input().split()))
x.append(x0)
x.sort()
d=[0]*n
for i in range(n):
    d[i]=x[i+1]-x[i]
res=d[0]
for i in range(1,n):
    res=math.gcd(res,d[i])
print(res)