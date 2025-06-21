from collections import defaultdict
from heapq import heappush, heappop


N, M = map(int, input().split())

jobs = defaultdict(list)
for _ in range(N):
    A, B = map(int, input().split())
    jobs[A].append(-B)

available_jobs = []
total_pay = 0
for day in range(1, M + 1):
    for pay in jobs[day]:
        heappush(available_jobs, pay)
    if available_jobs:
        total_pay -= heappop(available_jobs)
print(total_pay)
