n=int(input())
ki=[[] for _ in range(n)]
hen=[tuple(map(int,input().split())) for i in range(n-1)]
color={(hen[i][0]-1,hen[i][1]-1):0 for i in range(n-1)}
for i in range(n-1):
  a,b=hen[i][0],hen[i][1]
  ki[a-1].append(b-1)
  ki[b-1].append(a-1)
mcol=0
ne=0
for i in range(n):
  if len(ki[i])>mcol:
    mcol=len(ki[i])
    ne=i
print(mcol)
from collections import deque
d=deque()
d.append(ne)
visited=[False]*n
visited[ne]=True
col=[0]*n
while d:
  g=d.popleft()
  for i in ki[g]:
    if visited[i]:
      continue
    d.append(i)
    visited[i]=True
    if g>i:
      x,y=i,g
    else:
      x,y=g,i
    color[(x,y)]=col[g]%mcol+1
    col[g],col[i]=color[(x,y)],color[(x,y)]
for i in hen:
  print(color[(i[0]-1,i[1]-1)])