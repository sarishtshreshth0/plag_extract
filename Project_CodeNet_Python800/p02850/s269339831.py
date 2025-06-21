import sys
from collections import deque


N = int(input())
edge = [[] for _ in range(N)]
for i, s in enumerate(sys.stdin.readlines()):
    a, b = map(int, s.split())
    a -= 1; b -= 1
    edge[a].append((b, i))
    edge[b].append((a, i))


path = [None] * (N - 1)
q = deque()
q.append((0, 0))

while q:
    v, pc = q.popleft()
    c = 1
    for nv, i in edge[v]:
        if path[i] is None:
            c = c + 1 if c == pc else c
            path[i] = c
            q.append((nv, c))
            c += 1

print(max(path))
print(*path, sep='\n')
