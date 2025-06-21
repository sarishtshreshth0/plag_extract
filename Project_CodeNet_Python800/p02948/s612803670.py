import sys
f=lambda:map(int,sys.stdin.readline().split())
n,m=f()
lt=sorted(tuple(map(int,input().split())) for _ in range(n))[::-1]
from heapq import *
q=[]
s=t=0
while t<m:
  t+=1
  while lt and lt[-1][0]==t:
    a,b=lt.pop()
    heappush(q,-b)
  if q: s-=heappop(q)
print(s)