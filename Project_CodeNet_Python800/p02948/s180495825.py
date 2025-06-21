import heapq

n,m=map(int,input().split())

a=[[] for _ in range(m)]

d=[]

heapq.heapify(d)

for i in range(n):
  x,y=map(int,input().split())
  if x<=m:
    a[x-1].append(-y)
    
ans=0

for j in range(1,m+1):
  for h in a[j-1]:
    heapq.heappush(d,h)
  if len(d)>0:
    c=heapq.heappop(d)
    ans+=c
  
print(ans*(-1))