from collections import defaultdict
from heapq import heappush, heappop

N, M = map(int, input().split())
d = defaultdict(list)
q = []

for _ in range(N):
    a, b = map(int, input().split())
    d[a].append(b)

ans = 0
for i in range(1, M+1):
    for j in d[i]:
        heappush(q, -j)
    if q:
        ans += heappop(q)*-1

print(ans)
