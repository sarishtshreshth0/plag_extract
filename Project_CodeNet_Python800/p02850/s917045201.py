import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N)]
ab = [list(map(lambda x:int(x)-1, input().split())) for _ in range(N-1)]

col_max = 0
for i in range(N-1):
  a, b = ab[i]
  graph[a] += [b]
  graph[b] += [a]

for i in range(N):
  col_max = max(col_max, len(graph[i]))
print(col_max)

def bfs(s):
  q = deque([s])
  col = [-1]*N
  col[s] = 0
  edge_col = {}

  while q:
    c = 1
    u = q.pop()
    for v in graph[u]:
      if col[v] == -1:
        if c == col[u]:
          c += 1
        col[v] = c
        q.append(v)
        edge_col[(u, v)] = c
        edge_col[(v, u)] = c
        c += 1
  return edge_col

col = bfs(0)

for a, b in ab:
  print(col[(a, b)])