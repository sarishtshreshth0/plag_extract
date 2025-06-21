
from collections import deque

N = int(input())
X = [list(map(int, input().split())) for _ in range(N - 1)]

tree = [[] for _ in range(N + 1)]
for i, (a, b) in enumerate(X):
    tree[a].append((b, i))
    tree[b].append((a, i))

color = [0] * (N - 1)
nodes = [set() for _ in range(N + 1)]
visited = [False] * (N + 1)

q = deque([1])
visited[1] = True
while q:
    u = q.popleft()
    c = 1
    for v, i in tree[u]:
        if visited[v]:
            continue

        while c in nodes[v] or c in nodes[u]:
            c += 1
        color[i] = c
        nodes[u].add(c)
        nodes[v].add(c)
        visited[v] = True
        q.append(v)

print(max(len(v) for v in tree))
print(*color, sep="\n")
