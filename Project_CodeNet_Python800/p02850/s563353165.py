from collections import deque
from functools import reduce

n = int(input())
colors = [0]*(n-1)
mat = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    mat[a].append((i, b))
    mat[b].append((i, a))

q = deque()
max_len = reduce(lambda a, x:max(a, len(x)), mat, 0)
q.append(0)
while len(q) > 0:
    current = q.popleft()

    used_colors = set([colors[p[0]] for p in mat[current] if colors[p[0]] > 0])
    col = 1

    for p in mat[current]:
        if colors[p[0]] > 0:
            continue
        while col in used_colors:
            col += 1
        colors[p[0]] = col
        col += 1
        q.append(p[1])
print(max_len)
for col in colors:
    print(col)



