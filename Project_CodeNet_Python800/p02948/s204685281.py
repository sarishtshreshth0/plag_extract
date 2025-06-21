from heapq import heappop, heappush

n, nDays = map(int, input().split())
a = sorted(tuple(map(int, input().split())) for _ in range(n))
ret = 0
pq = []
pos = 0
for day in range(nDays + 1):
    while pos < n and a[pos][0] <= day:
        heappush(pq, -a[pos][1])
        pos += 1
    if pq:
        ret -= heappop(pq)
print(ret)