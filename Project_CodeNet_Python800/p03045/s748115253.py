import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

tree = [[] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x - 1].append(y - 1)
    tree[y - 1].append(x - 1)

visited = [False for _ in range(n)]


def dfs(v, p):
    for u in tree[v]:
        if u == p:
            continue
        elif visited[u]:
            continue
        else:
            visited[u] = True
            dfs(u, v)


res = 0
for i in range(n):
    if not visited[i]:
        visited[i] = True
        dfs(i, -1)
        res += 1

print(res)
