from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf,comb
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
d = LIST()
mod = 998244353

if d[0] != 0:
    print(0)
    exit()

c = Counter(d)
counts = [0]*(max(d)+1)
for k, v in c.items():
    counts[k] = v
if counts[0] > 1:
    print(0)
    exit()
ans = 1
for i in range(1, len(counts)):
    ans *= pow(counts[i-1], counts[i])
    ans %= mod

print(ans)