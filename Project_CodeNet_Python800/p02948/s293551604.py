from heapq import heappop,heappush
n,m=map(int,input().split())
L=[[] for _ in range(m)]
for _ in range(n):
  a,b=map(int,input().split())
  if a<=m:
    L[m-a].append(b)
s=0
h=[]
for i in range(m-1,-1,-1):
  for l in L[i][::-1]:
    heappush(h,-l)
  if len(h)>0:
    s-=heappop(h)
print(s)
