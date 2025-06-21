# D - Summer Vacation

import heapq

n, m = map(int, input().split())

w = [[0] for _ in range(m+1)] 

for _ in range(n):
    a, b = map(int, input().split())
    if a<=m:
        w[a].append(b)

ans = 0
hq = []
for i in range(1, m+1):
    for j in w[i]:
        heapq.heappush(hq, -j)
    ans += heapq.heappop(hq)

print(ans * -1)
