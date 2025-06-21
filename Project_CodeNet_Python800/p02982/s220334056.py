from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter,defaultdict
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
sys.setrecursionlimit(10**6)
# INF =  float("inf")
INF = 10**18
import bisect
import statistics
mod = 10**9+7
# mod = 998244353

N, D = map(int, input().split())

x = []
for i in range(N):
    x.append(list(map(int, input().split())))

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

ans = 0
for i in range(N):
    for j in range(i+1,N):
        d = 0
        for k in range(D):
            d += (x[i][k] - x[j][k])**2
        if abs(math.sqrt(d) - int(math.sqrt(d))) < 10**(-9):

            ans += 1
print(ans)
