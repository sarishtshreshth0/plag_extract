import heapq
n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)] + [[1000000, 1000000]]
li.sort()
idx = 0
hq = []
ans = 0
for i in range(m):
    while li[idx][0] <= i + 1:
        heapq.heappush(hq, -li[idx][1])
        idx += 1
    if hq:
        ans -= heapq.heappop(hq)
print(ans)
