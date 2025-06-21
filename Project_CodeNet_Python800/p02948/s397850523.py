from heapq import*
n,m=map(int,input().split())
x=[[]for _ in range(m)]
for _ in range(n):
  a,b=map(int,input().split())
  if a<=m:x[a-1]+=[-b]
q=[]
ans=0
for i in range(m):
  for j in x[i]:heappush(q,j)
  if q:ans-=heappop(q)
print(ans)