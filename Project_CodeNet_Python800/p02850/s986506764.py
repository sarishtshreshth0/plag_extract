from collections import deque

def bfs(idx,k,colored):
  q = deque()
  visited[idx] = True
  q.append(idx)
  while q:
    r = q.pop()
    color = 0
    for n in graph[r].keys():
      if not visited[n]:
        if color == colored[r]: color+=1
        colored[n] = color
        graph[r][n] = color
        graph[n][r] = color
        color += 1

        visited[n] = True
        q.append(n)

        
N = int(input())
graph = {}
colored = [-1]*(N+1)
visited = [False]*(N+1)
for i in range(N+1):
  graph[i] = {}
ab = []
for i in range(N-1):
  a,b = map(int,input().split())
  ab.append((a,b))
  graph[a][b] = -1
  graph[b][a] = -1
  
k = max([len(graph[i]) for i in range(1,N+1)])

bfs(1,k,colored)
print(k)
for a,b in ab:
  print(graph[a][b]+1)
