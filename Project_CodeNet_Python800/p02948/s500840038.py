import heapq
n, m = map(int, input().split())

jobs = [[] for _ in range(m+1)]
for _ in range(n):
    a, b = map(int, input().split())
    if a <= m:
        jobs[a].append(-b)

h = []
ans = 0
for i in range(1, m+1):
    for j in jobs[i]:
        heapq.heappush(h, j)
    if len(h) > 0:
        ans += -heapq.heappop(h)

print(ans)