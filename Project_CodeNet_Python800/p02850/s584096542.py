from collections import deque

N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
  a, b = map(int, input().split())
  a, b = a-1, b-1
  G[a].append([b, i])
  G[b].append([a, i])

ans = [0]*(N-1)
q = deque([(0, -1)])
while q:
  v, pc = q.popleft()
  c = 1 if pc != 1 else 2
  for nv, i in G[v]:
    if ans[i] == 0:
      ans[i] = c
      q.append((nv, c))
      c += 1 if c+1 != pc else 2

print(max(ans))
print(*ans, sep="\n")