f=lambda:map(int,input().split())
n,m=f()
lt=sorted(list(f()) for _ in range(n))[::-1]
from heapq import *
q,s=[],0
for i in range(m):
  while lt and lt[-1][0]<i+2: a,b=lt.pop(); heappush(q,-b)
  if q: s-=heappop(q)
print(s)