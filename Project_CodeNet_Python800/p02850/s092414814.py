from collections import deque

N = int(input())

int1 = lambda x: int(x) - 1
edges = [[] for _ in range(N)]
nodes = [None] * N
for i in range(1, N):
    a, b = map(int1, input().split())
    edges[a].append(i)
    edges[b].append(i)
    nodes[i] = (a, b)

# dfs
C = max(len(x) for x in edges)
colors = [None] * N
d = deque([(0, 0)])
while d:
    v, parent_color = d.pop()
    i = 1
    for x in edges[v]:
        if colors[x] is None:
            if i == parent_color:
                i += 1
            colors[x] = i
            a, b = nodes[x]
            d.append((b if a == v else a, i))
            i += 1


print(C)
for i in range(1, N):
    print(colors[i])
