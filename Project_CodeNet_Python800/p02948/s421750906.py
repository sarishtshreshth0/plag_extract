from collections import defaultdict
import heapq
n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    a, b = map(int, input().split())
    d[a-1].append(-b)
cnt = 0
a = []
heapq.heapify(a)
for i in range(m):
    for j in d[i]:
        heapq.heappush(a, j)
    if a:
        cnt += -heapq.heappop(a)
print(cnt)