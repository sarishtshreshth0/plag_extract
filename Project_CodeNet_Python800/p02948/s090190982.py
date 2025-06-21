import heapq
from collections import defaultdict

N, M = map(int, input().split())
d = defaultdict(list)
for i in range(N):
    A, B = map(int, input().split())
    d[A].append(-B)

ans = 0
work = []
for i in range(1, M+1):
    for j in range(len(d[i])):
        heapq.heappush(work, d[i][j])
    if len(work):
        ans -= heapq.heappop(work)
print(ans)