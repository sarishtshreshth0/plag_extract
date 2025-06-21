n=int(input())

import sys
sys.setrecursionlimit(10 ** 7)

graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append((b - 1, i))
    graph[b - 1].append((a - 1, i))
# print(graph)

max_color=0
for graph_i in graph:
    max_color=max(max_color, len(graph_i))
print(max_color)

colors=[-1]*(n-1)

def dfs(v, color, pre):
    if color!=0:
        nc=0
    else:
        nc=1
    for e in graph[v]:
        # print(e,nc)
        if e[0]==pre:
            continue
        colors[e[1]]=nc
        dfs(e[0],nc,v)
        nc+=1
        if nc==color:
            nc+=1

dfs(0,-1,-1)

for c in colors:
    print(c+1)
