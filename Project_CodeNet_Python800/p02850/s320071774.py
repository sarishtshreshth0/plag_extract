N = int(input())
ab = [list(map(int,input().split())) for i in range(N-1)]

graph = [[] for _ in range(N+1)]
for a,b in ab:
    graph[a].append(b)
    graph[b].append(a)

from collections import deque
todo = deque([1])
seen = deque([])
parent = [0] * (N+1)

# 親と子の関係を作る
while todo:
    x = todo.popleft()
    seen.append(x)
    for y in graph[x]:
        if y == parent[x]:
            continue
        parent[y] = x
        todo.append(y)
        
# 根以外の頂点は、唯一の親を持つことから、
# vの親がpであるとき → color[v] に辺 pvの色を持たせると定めて色を管理
color = [-1] * (N+1)
for x in seen:
    ng = color[x]
    c = 1
    for y in graph[x]:
        if y == parent[x]:
            continue
        if c == ng:
            c += 1
        color[y] = c
        c += 1

ans = []
for a,b in ab:
    ans.append(color[b])

print(max(ans))
for i in ans:
    print(i)
