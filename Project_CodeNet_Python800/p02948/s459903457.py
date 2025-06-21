from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
N, M = map(int, input().split())
dates = [[] for _ in range(10**5+1)]
for i in range(N):
    x,y = map(int, input().split())
    dates[x].append(y)

h = []
heapify(h)
ans = 0
for i in range(1,M+1):
    for b in dates[i]:
        heappush(h,-b)
    if len(h):
        ans -= heappop(h)
print(ans)