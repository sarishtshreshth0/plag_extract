import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

from collections import Counter


n, m, k = map(int, input().split())

graph1 = [[] for _ in range(n)]
for _ in range(m):
    a, b = [int(x) - 1 for x in input().split()]
    graph1[a].append(b); graph1[b].append(a)

graph2 = [[] for _ in range(n)]
for _ in range(k):
    c, d = [int(x) - 1 for x in input().split()]
    graph2[c].append(d); graph2[d].append(c)

def dfs(now):
    X[now] = x
    for next in graph1[now]:
        if X[next]:
            continue
        dfs(next)

X = [0] * n
x = 1
for i in range(n):
    if X[i]:
        continue
    dfs(i)
    x += 1

cnt = Counter(X)

ans = []
for i in range(n):
    x = X[i]
    tmp = cnt[x] - 1
    tmp -= len(graph1[i])
    tmp -= sum(X[j] == x for j in graph2[i])
    ans.append(tmp)

print(*ans)
