from collections import defaultdict
import sys
sys.setrecursionlimit(150000)

n,m,k = map(int, input().split())
f_G = defaultdict(lambda:[])
b_G = defaultdict(lambda:[])

for i in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    f_G[a].append(b)
    f_G[b].append(a)

for i in range(k):
    c,d = map(int, input().split())
    c -= 1
    d -= 1
    b_G[c].append(d)
    b_G[d].append(c)

def dfs(graph,v,cnt,list):
    global node
    seen[v] = True
    node += 1

    for nv in f_G[v]:
        if seen[nv]:
            continue
        dfs(graph,nv,cnt,list)

    list[v] = cnt

d = [0]
list = [0] * n
seen = [False] * n
cnt = 0
for i in range(n):
    if seen[i]:
        continue
    cnt += 1
    node = 0
    dfs(f_G,i,cnt,list)
    d.append(node)

ans = [0] * n
for i in range(n):
    a = d[list[i]]
    a -= (len(f_G[i]) + 1)

    for j in (b_G[i]):
        if list[i] == list[j]:
            a -= 1

    ans[i] = a

print(*ans)
