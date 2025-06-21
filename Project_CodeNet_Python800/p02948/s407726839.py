import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)
from bisect import bisect_right

N, M = mapint()

from heapq import heappop, heappush
days = [[] for _ in range(M)]
for _ in range(N):
    a, b = mapint()
    if a>M:
        continue
    days[a-1].append(-b)

queue = []

ans = 0
for i in range(M):
    lis = days[i]
    for b in lis:
        heappush(queue, b)
    if queue:
        ans += heappop(queue)

print(-ans)