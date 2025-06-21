import sys
import heapq

sys.setrecursionlimit(10000000)

n,m= map(int,input().split())

jobs = [[] for _ in range(m) ]

for i in range(n):
    a,b= map(int,input().split())
    if a > m:continue
    jobs[m-a].append(b)
q=[]
heapq.heapify(q)
ans=0

for i in range(m-1,-1,-1):
    for b in jobs[i]:
        heapq.heappush(q,-b)

    if q:
        ans+= -heapq.heappop(q)

print(ans)