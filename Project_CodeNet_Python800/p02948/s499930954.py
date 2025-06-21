#137-d
import heapq as hp

n,m=[int(i) for i in input().split()]

lists=[[] for _ in range(m)]
for i in range(n):
    a,b = [int(i) for i in input().split()]
    if a<=m:
        lists[a-1].append(b)
        
h = []
hp.heapify(h)

ans= 0
for i in range(m):
    for v in lists[i]:
        hp.heappush(h,-v)
    if len(h)>0:
        ans -= hp.heappop(h)
print(ans)    
