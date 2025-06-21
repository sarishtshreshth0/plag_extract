n,m=map(int,input().split())
jobs=[]
for i in range(n):
    a,b=map(int,input().split())
    jobs.append((a,-b))
jobs.sort(reverse=True)

import heapq
hp=[]
ans=0
for i in range(1,m+1):
    while jobs and jobs[-1][0]<=i:
        heapq.heappush(hp,jobs.pop()[1])
    if hp:
        ans-=heapq.heappop(hp)
print(ans)