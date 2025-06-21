n = int(input())
edges = [[] for _ in range(n)]
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    a, b = ab[i]
    for j in range(n):
        c, d = cd[j]
        if a < c and b < d:
            edges[i].append(j)
matched = [-1] * n
def dfs(v):
    for u in edges[v]:
        if visited[u]:
            continue
        visited[u] = True
        if matched[u] == -1 or dfs(matched[u]):
            matched[u] = v
            return True
    return False

ans = 0
for s in range(n):
    visited = [False] * n
    if dfs(s):
        ans += 1
print(ans)