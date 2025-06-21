import sys
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    x, y = x-1, y-1
    edge[x].append(y)
    edge[y].append(x)

visited = [0] * N
def dfs(v):
    if visited[v] == 1:
        return
    visited[v] = 1
    for nv in edge[v]:
        dfs(nv)
ans = 0
for i in range(N):
    if visited[i] == 1:
        continue
    ans += 1
    dfs(i)

print(ans)
