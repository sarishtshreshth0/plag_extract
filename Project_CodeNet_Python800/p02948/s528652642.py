
from heapq import heappop, heappush

N, M = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

X.sort(reverse=True)
ans = 0
pq = []
for n in range(M + 1):
    while X and X[-1][0] <= n:
        a, b = X.pop()
        heappush(pq, -b)

    if pq:
        ans -= heappop(pq)

print(ans)
