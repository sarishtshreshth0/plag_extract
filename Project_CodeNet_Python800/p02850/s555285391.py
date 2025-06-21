from collections import deque
n=int(input())
graph=[[] for i in range(n)]#0-indexed
edges=[tuple(map(int,input().split())) for i in range(n-1)]#1-indexed
edge_color={(edges[i][0]-1,edges[i][1]-1):0 for i in range(n-1)}#0-indexed
vertex=[0 for i in range(n)]
for i in edges:
  a,b=i[0],i[1]
  a-=1;b-=1
  graph[a].append(b)
  graph[b].append(a)
color=0;most_connected=0
for i in range(n):
  if len(graph[i])>color:
    color=len(graph[i])
    most_connected=i
visited=[False]*n
bfs=deque([most_connected])
while bfs:
  v=bfs.popleft()
  visited[v]=True
  for i in graph[v]:
    if visited[i]:continue
    I,V=i,v
    if i<v:
      I,V=v,i
    
    edge_color[(V,I)]=vertex[v]%color+1
    vertex[V],vertex[I]=edge_color[(V,I)],edge_color[(V,I)] 
    bfs.append(i)
print(color)
for i in edges:
  print(edge_color[(i[0]-1,i[1]-1)])
