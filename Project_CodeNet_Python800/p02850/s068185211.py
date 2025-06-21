# D - Coloring Edges on Tree

import sys

sys.setrecursionlimit(10 ** 5)

N = int(input())
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append((b, i))
    G[b].append((a, i))

ans = [-1] * (N - 1)

def dfs(key, color=-1, parent=-1):
    k = 1
    for i in range(len(G[key])):
        if G[key][i][0] == parent:
            continue
        if color == k:
            k += 1
        ans[G[key][i][1]] = k
        dfs(G[key][i][0], k, key)
        k += 1

dfs(0)

print(max(ans))
for a in ans:
    print(a)
