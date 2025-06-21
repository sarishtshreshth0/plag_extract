import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
from itertools import permutations,  combinations, accumulate
from functools import *
from collections import deque, defaultdict, Counter
from heapq import heapify, heappop, heappush, heappushpop

INF = float('inf')
NIL = - 1


N, M = map(int, input().split())
jobs = [[] for _ in range(M + 1)]
for _ in range(N):
    a, b = map(int, input().split())
    if a <= M:
        jobs[M - a].append(b)

heap = []
for day in range(M + 1):
    for job in jobs[day]:
        if len(heap) <= day:
            heappush(heap, job)
        else:
            heappush(heap, job)
            heappop(heap)

print(sum(heap))
