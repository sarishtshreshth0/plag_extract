import sys
input = sys.stdin.readline

import heapq
N,M = (int(x) for x in input().split())
jobs = [[] for i in range(M)]
count = 0
h = []
for i in range(N):
    A,B = (int(x) for x in input().split())
    if A <= M:
        jobs[A-1].append(B*(-1))
heapq.heapify(h)
for i in range(M):
    if jobs[i]:
        for job in jobs[i]:
            heapq.heappush(h,job)
    if h:
        count -= heapq.heappop(h)
print(count)