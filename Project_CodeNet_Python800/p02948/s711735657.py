from collections import defaultdict
from heapq import heappush, heappop, merge

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

day = defaultdict(list)
for a, b in ab:
    day[a].append(b)

work, ans = [], 0
for i in range(1, m + 1):
    for j in day[i]:
        heappush(work, -j)
    if len(work) > 0:
        ans -= heappop(work)
print(ans)
