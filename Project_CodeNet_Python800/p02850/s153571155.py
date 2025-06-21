#グラフ構造DFSを使う
import sys
sys.setrecursionlimit(500000)
N = int(input())
ans = [-1] * (N-1)
g = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    g[a-1].append((b-1, i))
    g[b-1].append((a-1, i))

def bfs(v, c, p):
    n_c = 1
    for i in range(len(g[v])):
        to = g[v][i][0]
        ID = g[v][i][1]
        if to == p:
            continue
        if n_c == c:
            n_c += 1
        ans[ID] = n_c
        bfs(to, n_c, v)
        n_c += 1

bfs(0, 0, -1)
print(max(ans))
for i in range(N-1):
    print(ans[i])