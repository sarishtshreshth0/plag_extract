from heapq import *
n, m = map(int, input().split())
a = sorted([list(map(int, input().split()))for _ in range(n)])
a.append([10**9])
r,j,x=0,0,[]
heapify(x)
for i in range(m):
    while a[j][0]<=i+1:heappush(x,-a[j][1]);j+=1
    if x:r-=heappop(x)
print(r)