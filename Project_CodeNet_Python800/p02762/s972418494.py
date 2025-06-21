import sys
from collections import Counter
n,m,k = map(int,input().split())
fgraph = [list() for i in range(n)]
bgraph = [list() for i in range(n)]
cgraph = [list() for i in range(n)]

rks = [None] * n
sys.setrecursionlimit(10**9)

# r: どの連結成分に存在するか
def dfs(graph, s, r):
    if rks[s] is None:
        rks[s] = r
    for i in range(len(graph[s])):
        if rks[graph[s][i]-1] is not None:
            continue
        dfs(graph,graph[s][i]-1,r)

for i in range(m):
    a,b = map(int,input().split())
    fgraph[a-1].append(b)
    fgraph[b-1].append(a)

# 連結成分にindexをつける
c = -1
for i in range(n):
    if rks[i] is None:
        c += 1
        dfs(fgraph, i, c)

for i in range(k):
    c,d = map(int,input().split())
    # おなじ連結成分に属するものだけ処理すれば良い
    if rks[c-1] == rks[d-1]:
        bgraph[d-1].append(c)
        bgraph[c-1].append(d)

counter = Counter(rks)
for i in range(n):
    print(counter[rks[i]] - len(fgraph[i]) - len(bgraph[i]) - 1, end=' ')
