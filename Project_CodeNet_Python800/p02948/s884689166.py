import heapq

n, m = map(int, input().split())
lis = []
for i in range(m + 1):
    lis.append([])

for i in range(n):
    a, b = map(int, input().split())
    if a <= m:
        lis[a].append(-b)

cnd = []
heapq.heapify(cnd)
res = 0

for j in range(1, m + 1):
    for e in lis[j]:
        heapq.heappush(cnd, e)
    if cnd:
        res += -heapq.heappop(cnd)
print(res)
