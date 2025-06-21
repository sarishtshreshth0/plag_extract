import collections
import sys
import numpy as np
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
MOD = 10**9+7
import itertools
import math

q,h,s,d = map(int,input().split())
n = int(input())
h = min(q*2,h)
s = min(h*2,s)
if n == 1:
    print(s)
    sys.exit()

if 2*s > d:
    print(d*(n//2) + (n%2)*s)
else:
    print(n*s)