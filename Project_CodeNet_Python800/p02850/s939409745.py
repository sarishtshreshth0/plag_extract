n=int(input())
G=[[] for i in range(n+1)]
G_order=[]
for i in range(n-1):
  a,b=map(int,input().split())
  G[a].append(b)
  G_order.append(b)

from collections import deque
q=deque([1])
color=[0]*(n+1)
while q:
  cur=q.popleft()
  c=1
  for nx in G[cur]:
    if c==color[cur]:
      c+=1
    color[nx]=c
    c+=1
    q.append(nx)

print(max(color))
for i in G_order:
  print(color[i])