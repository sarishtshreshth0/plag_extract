import sys
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    edges[x].append(y)
    edges[y].append(x)

visited = [False] * N

def dfs(u):
    if visited[u]:
        return

    visited[u] = True
    for v in edges[u]:
        if visited[v]:
            continue
        dfs(v)

ans = 0
for u in range(N):
    if visited[u]:
        continue
    ans += 1
    dfs(u)
print(ans)