N,M = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(N)]

AB.sort(key=lambda x: x[0])

import heapq
from collections import deque

AB = deque(AB)

ans = 0
task = []
heapq.heapify(task)

for i in range(M):
    while len(AB) > 0 and AB[0][0] <= i+1:
        t = AB.popleft()
        heapq.heappush(task,-t[1])
    if len(task) > 0:
        ans += heapq.heappop(task)
print(-ans)


