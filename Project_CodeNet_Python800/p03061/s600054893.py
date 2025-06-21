import sys
from functools import lru_cache, cmp_to_key
from heapq import merge, heapify, heappop, heappush
from math import *
from collections import defaultdict as dd, deque, Counter as C
from itertools import combinations as comb, permutations as perm
from bisect import bisect_left as bl, bisect_right as br, bisect
from time import perf_counter
from fractions import Fraction
# import numpy as np
sys.setrecursionlimit(int(pow(10,6)))
# sys.stdin = open("input.txt", "r")
# sys.stdout = open("out.txt", "w")
mod = int(pow(10, 9) + 7)
mod2 = 998244353
def data(): return sys.stdin.readline().strip()
def out(*var, end="\n"): sys.stdout.write(' '.join(map(str, var))+end)
def l(): return list(sp())
def sl(): return list(ssp())
def sp(): return map(int, data().split())
def ssp(): return map(str, data().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]

# @lru_cache(None)
t=1
# t=int(input())
for _ in range(t):
    n=l()[0]
    A=l()
    L=[A[0] for i in range(n)]
    R=[A[-1] for i in range(n)]
    for i in range(1,n):
        L[i]=gcd(L[i-1],A[i])
        R[n-i-1]=gcd(R[n-i],A[n-i-1])
    mx=0
    # print(*L)
    # print(*R)
    for i in range(n):
        if i==0:
            mx=max(mx,R[i+1])
        elif i==n-1:
            mx=max(mx,L[i-1])
        else:
            g=gcd(L[i-1],R[i+1])
            mx=max(mx,g)
    print(mx)


