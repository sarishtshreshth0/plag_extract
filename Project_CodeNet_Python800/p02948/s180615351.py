import heapq as hq
n,m = map(int,input().split())
ab = []
for i in range(n):
    a,b = map(int,input().split())
    ab.append((a,-b))
ab.sort()
ans = 0
idx = 0
q = []
for i in range(1,m+1):
    while idx<n and ab[idx][0] ==i:
        a,mb = ab[idx]
        hq.heappush(q,mb)
        idx+=1
    if q!=[]:
        ans += -1*hq.heappop(q)

print(ans)
