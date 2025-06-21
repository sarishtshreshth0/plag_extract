import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import heapq

n, m = map(int, readline().split())
ab = [[] for _ in range(10 ** 5 + 1)]
for _ in range(n):
    a, b = map(int, readline().split())
    ab[a - 1].append(-b)
ans = 0
q = []
for mm in range(m):
    while ab[mm]:
        heapq.heappush(q, ab[mm].pop())
    if q:
        ans += heapq.heappop(q)
print(-ans)
