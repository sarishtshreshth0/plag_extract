from heapq import heappop, heappush
n, m = map(int, input().split())
d = []
for _ in range(n):
    a, b = map(int, input().split())
    d.append((m - a, b))
d.sort()
ans = 0
q = []
for i in range(m - 1, -1, -1):
    while d and d[-1][0] == i:
        heappush(q, -d.pop()[1])
    if q:
        ans -= heappop(q)
print(ans)
