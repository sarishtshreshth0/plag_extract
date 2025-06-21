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
INF =  float("inf")
import bisect

N = int(input())
ad = [[] for i in range(N+1)]

edges = []
for i in range(N-1):
    a, b = list(map(int, input().split()))
    edges.append((a,b))
    ad[a].append(b)
    ad[b].append(a)

ans_max = 0
for i in range(1,N+1):
    ans_max = max(ans_max, len(ad[i]))

print(ans_max)

visited = [0 for i in range(N+1)]
seen = [0 for i in range(N+1)]
edge_color = defaultdict(int)
node_color = [0 for i in range(N+1)]

def bfs(u):
    stack = deque([u])
    seen[u] = 1
    node_color[u] = 0

    while len(stack) > 0:
        v = stack.popleft()

        c = 1
        for w in ad[v]:
            if seen[w] == 0:
                stack.append(w)
                if c != node_color[v]:
                    edge_color[(v, w)] = c
                    node_color[w] = c
                else:
                    c += 1
                    edge_color[(v, w)] = c
                    node_color[w] = c
                c += 1
                seen[w] = 1

        if stack == []: break

bfs(1)

for edge in edges:
    if edge_color[edge] != 0:
        print(edge_color[edge])
    else:
        print(edge_color[edge.reverse()])