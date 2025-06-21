import heapq
n,m=map(int,input().split())
d=[]
for i in range(n):
  a,b=map(int,input().split())
  d.append([a,b])
d=sorted(d, key=lambda student: student[0])
pointer=0
queue=[]
ans=0
for i in range(m+1):
  while pointer<n and d[pointer][0]==i:
    heapq.heappush(queue,-d[pointer][1])
    pointer+=1
    if pointer>=n:
      break
  if queue:
    ans+=heapq.heappop(queue)
print(-ans)