import sys
sys.setrecursionlimit(10**6)
N = int(input())
edge = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    edge[a].append((b, 1+i))

color = [0] * N

def dfs(v, c, idx):
    color[idx] = c
    now = 0
    for nv, i in edge[v]:
        now += 1
        if now == c:
            now += 1
        dfs(nv, now, i)

dfs(0, 0, 0)
color[0] = max(color)
print(*color, sep="\n")
