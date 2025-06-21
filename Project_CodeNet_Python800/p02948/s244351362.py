from heapq import heappush, heappop

n, m = map(int, input().split())
jobs = []
for i in range(n):
    a, b = map(int, input().split())
    jobs.append([a, b])

jobs = sorted(jobs, key=lambda x:x[0])

hq = []
res, j = 0, 0
for i in range(1, m + 1):
    while j < n and jobs[j][0] <= i:
        heappush(hq, -jobs[j][1])
        j += 1
    if len(hq) > 0:
        res += -heappop(hq)
print(res)