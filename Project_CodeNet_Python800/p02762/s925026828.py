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

N, M, K = map(int, input().split())

al = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    al[a].append(b)
    al[b].append(a)

block = [[] for i in range(N+1)]
for i in range(K):
    c, d = map(int, input().split())
    block[c].append(d)
    block[d].append(c)

seen = [0 for i in range(N+1)]
num_connect = [0 for i in range(N+1)]
cluster = [0 for i in range(N+1)]

def bfs(u, c):
    visited = []
    stack = deque([u])
    seen[u] = 1
    count = 1

    while len(stack) > 0:
        v = stack.popleft()
        visited.append(v)
        cluster[v] = c
        for w in al[v]:
            if seen[w] == 0:
                stack.append(w)
                count += 1
                seen[w] = 1

    for v in visited:
        num_connect[v] = count

c = 1
for i in range(1,N+1):
    if seen[i] == 0:
        bfs(i, c)
        c += 1

for i in range(1,N+1):
    bl = 0
    for d in block[i]:
        if cluster[i] == cluster[d]:
            bl += 1
    print(num_connect[i] - 1 - len(al[i]) - bl, end=" ")