# coding: utf-8
import heapq
n, m = map(int, input().split())
jobs = [[] for i in range(m)]
for i in range(n):
    a, b = map(int, input().split())
    if a > m:
        continue
    jobs[m-a].append(b)
ans = 0
l = []
for i in range(m-1, -1, -1):
    for j in jobs[i]:
        heapq.heappush(l, -j)
    if len(l):
        ans += -heapq.heappop(l)
print(ans)