import heapq
from collections import defaultdict

n, m = map(int, input().split())
ans = 0
jobs = defaultdict(list)
to_do = []
heapq.heapify(to_do)
for i in range(n):
    array = list(map(int, input().split()))
    array[1] *= -1
    jobs[array[0]].append(array[1])

for i in range(1, m+1):
    if len(jobs[i]) > 0:
        for j in jobs[i]:
            heapq.heappush(to_do, j)
    if len(to_do) > 0:
        ans += -1 * heapq.heappop(to_do)

print(ans)

