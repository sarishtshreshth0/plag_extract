import heapq
x = [[] for _ in range(10**5+1)]
n,m = map(int,input().split())

for i in range(n):
    a,b = map(int,input().split())
    x[a].append(b)
    
cur = []
heapq.heapify(cur)

ans = 0
for l in range(1,m+1):
    for k in x[l]:
        heapq.heappush(cur, k*(-1))
    
    if cur != []:
        mi = heapq.heappop(cur)
        ans += mi * (-1)
        
print(ans)