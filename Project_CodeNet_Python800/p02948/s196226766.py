import heapq
n,m=map(int,input().split())
w=[[] for i in range(m)]
for i in range(n):
  a,b=map(int,input().split())
  a-=1
  if a>=m:
    continue
  w[a].append(-b)

h=[]
c=0
for i in range(m):
  for j in w[i]:
    heapq.heappush(h,j)
  try:
    c+=heapq.heappop(h)
  except:
    pass
print(-c)