from collections import deque
from operator import itemgetter
import heapq

N, M = map(int, input().split())
jobs = [tuple(map(int, input().split())) for _ in range(N)]
jobs.sort()

q = deque(jobs)
r = []

heapq.heapify(r)

res = 0
for i in range(M):
    while q:
        job = q.popleft()
        if job[0] > i + 1:
            q.appendleft(job)
            break
        else:
            heapq.heappush(r, -job[1])

    if len(r) >= 1:
        res -= heapq.heappop(r)

print(res)