from collections import deque
N,M = map(int,input().split())
G = [[] for i in range(N+1)]
for i in range(M):
  x,y,z = map(int,input().split())
  G[x].append(y)
  G[y].append(x)

cnt = 0
seen = [False]*(N+1)
for i in range(1,N+1):
  if seen[i] == False:
    seen[i] = True
    cnt += 1
    d = deque([i])
    while len(d)>0:
      v = d.popleft()
      for j in G[v]:
        if seen[j] == False:
          seen[j] = True
          d.append(j)
###
print(cnt)