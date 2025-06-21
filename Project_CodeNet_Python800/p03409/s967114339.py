# -*- coding: utf-8 -*-
# C - 2D Plane 2N Points
import sys 
from bisect import bisect,bisect_left
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())
query = [(0,0)]*N*2
# 赤0 青1
for _ in range(N):
    a,b =map(int,readline().split())
    query[a] = (0,b)
for _ in range(N):
    a,b =map(int,readline().split())
    query[a] = (1,b)

A = []
ans = 0
for i in range(2*N):
    q,y = query[i]
    if q == 0:
        A.append(y)
        A = sorted(A)
    else:
        ind = bisect_left(A,y)
        if ind != 0:
            A.pop(ind-1)
            ans += 1
print(ans)