n = int(input())
G = [[] for _ in range(n)]
edge  = []
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    edge.append(b)

from collections import deque

q = deque()
color = [0]*n
q.append(0)
while q:
    cur = q.popleft()
    c = 1
    for nx in G[cur]:
        if color[cur] == c:
            c += 1
        color[nx] = c
        c += 1
        q.append(nx)

print(max(color))
for e in edge:
    print(color[e])