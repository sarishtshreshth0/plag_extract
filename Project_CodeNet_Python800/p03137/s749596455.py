#import sys
#import numpy as np
import math
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
d=[0]*m
for i in range(1,m):
  d[i]=a[i]-a[i-1]
d.sort(reverse=True)
print(sum(d[n-1:]))