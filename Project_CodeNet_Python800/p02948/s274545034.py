N, M = map(int, input().split())
jobs = sorted([list(map(int, input().split())) for i in range(N)], reverse=True)

from heapq import *
q = []
heapify(q)
ans = 0
for i in range(1, M+1):
    while jobs and jobs[-1][0] <= i:
        heappush(q, -1*jobs.pop()[1])
    if q:
        ans += -1 * heappop(q)
print(ans)