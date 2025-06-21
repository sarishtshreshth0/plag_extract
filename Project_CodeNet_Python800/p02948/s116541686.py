import sys
from heapq import *

readline = sys.stdin.readline
N, M = map(int, readline().split())
days = [[] for _ in range(M)]
for _ in range(N):
    a, b = map(int, readline().split())
    if a <= M:
        days[a-1].append(b)
ans = 0
hq = []
heapify(hq)
for day in days:
    for pay in day:
        heappush(hq, -pay)
    if hq:
        ans += -heappop(hq)
print(ans)
