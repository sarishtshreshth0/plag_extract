from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

def pow_k(x, n, mod):
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x = x * x % mod
        n //= 2

    return K * x % mod

n, a, b = MAP()
ans = pow_k(2,n,10**9+7) - 1

x0 = 1
y0 = 1
x1 = 1
y1 = 1
for i in range(1, max(a,b)+1):
    if i <= a:
        x0 = x0 * (n - i + 1) % (10**9+7)
        y0 = y0 * i % (10**9+7)
    if i <= b:
        x1 = x1 * (n - i + 1) % (10**9+7)
        y1 = y1 * i % (10**9+7)

ans -= x0*pow_k(y0,10**9+7-2,10**9+7) + x1*pow_k(y1,10**9+7-2,10**9+7)
print(ans % (10**9+7))