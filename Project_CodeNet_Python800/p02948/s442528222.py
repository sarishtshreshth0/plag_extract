n,m = map(int,input().split())
ans = 0
import heapq
g = [[] for i in range(100000)]
for i in range(n):
    a,b = map(int,input().split())
    a -= 1
    g[a].append(-b)
for i in range(100000):
    heapq.heapify(g[i])
p = []
heapq.heapify(p)
for i in range(m):
    if len(g[i]) != 0:
        heapq.heappush(p,[heapq.heappop(g[i]),i])
    if len(p) != 0:
        x = heapq.heappop(p)
        ans += -x[0]
        if len(g[x[1]]) != 0:
            heapq.heappush(p,[heapq.heappop(g[x[1]]),x[1]])            
print(ans)