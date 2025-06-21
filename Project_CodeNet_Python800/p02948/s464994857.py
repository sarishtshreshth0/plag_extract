import heapq
n, m = map(int, input().split())
jobs = [[] for _ in range(m)]
for i in range(n):
    a, b = map(int, input().split())
    if a-1 < m:
        jobs[a-1].append(-b)

heap = []
ans = 0
for i in range(m):
    for reword in jobs[i]:
        heapq.heappush(heap, reword)
    if len(heap) > 0:
        b = heapq.heappop(heap)
        ans += -b
print(ans)