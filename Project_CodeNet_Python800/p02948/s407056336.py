from heapq import*
(n,m),*t=[map(int,s.split())for s in open(0)]
q=[0]*7**6
v=[[]for _ in q]
z=0
for a,b in t:v[a-1]+=[b]
for i in v[:m]:
  for j in i:heappush(q,-j)
  z-=heappop(q)
print(z)