# -*- coding: utf-8 -*-
import collections

#
N = int(input())
edges = []
graph = [[] for _ in range(N)]
color = [{} for _ in range(N)]
for _ in range(N-1):
    a,b = map(int, input().split())
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)

    color[a][b] = -1
    color[b][a] = -1

    edges.append((a, b))

#
buf = collections.deque()
buf.append(0)

while buf:
    src = buf.popleft()
    used = [color[src][dst] for dst in graph[src]
                if color[src][dst] != -1]
    dst_color = 1
    while dst_color in used:
        dst_color += 1

    for dst in graph[src]:
        if color[src][dst] == -1:
            color[src][dst] = dst_color
            color[dst][src] = dst_color
            buf.append(dst)

            used.append(dst_color)
            while dst_color in used:
                dst_color += 1



#
print(max([max(c.values()) for c in color]))
for a,b in edges:
    print(color[a][b])


