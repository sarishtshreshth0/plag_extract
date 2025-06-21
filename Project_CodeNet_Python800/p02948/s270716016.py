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

task = []
heapq.heapify(task)

N, M = map(int, input().split())

A = [[] for i in range(M+1)]
for i in range(N):
    a, b = map(int, input().split())
    if a > M: continue
    A[a].append(b)

ans = 0
for i in range(1,M+1):
    for b in A[i]:
        heapq.heappush(task, -b)
    if len(task) > 0:
        ans += heapq.heappop(task)*(-1)

print(ans)



