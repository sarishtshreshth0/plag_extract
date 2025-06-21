#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

n = I()
edges = [[] for _ in range(n)]
ab = [[i] + LI() for i in range(n-1)]
cnt = [0] * n
for i, a, b in ab:
    edges[a-1].append((i, b-1))
    edges[b-1].append((i, a-1))
    cnt[a-1] += 1
    cnt[b-1] += 1

k = max(cnt)
print(k)
que = deque([(0, -1, 0)])
edges_color = [None] * (n-1)
while que:
    v, p, col = que.popleft()
    cnt = 1
    for i, u in edges[v]:
        if edges_color[i] != None:
            continue
        if u == p:
            continue
        if cnt != col:
            edges_color[i] = cnt
        else:
            edges_color[i] = cnt + 1
            cnt += 1
        que.append((u, v, cnt))
        cnt += 1
for c in edges_color:
    print(c)