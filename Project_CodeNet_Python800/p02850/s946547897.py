from collections import deque

N = int(input())
routings = [[] for _ in range(N+1)]
colors = [0 for _ in range(N+1)]
vertexes = [tuple(map(int, input().split())) for _ in range(N-1)]

for a, b in vertexes:
  routings[a].append(b)
  routings[b].append(a)
  
edges = deque([1])
colors[1] = 0
answer = 0
while len(edges) > 0:
  edge = edges.pop()
  color = colors[edge]
  nc = 1
  answer = max(answer, len(routings[edge]))
  for ne in routings[edge]:
    if colors[ne] == 0 and ne != 1:
      if nc == color:
        nc += 1
      colors[ne] = nc
      edges.append(ne)
      nc += 1
print(answer)
for a, b in vertexes:
  print(colors[b])
