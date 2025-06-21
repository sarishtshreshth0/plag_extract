from collections import deque

n = int(input())
tree = [[] for _ in range(n)]
color = dict()
edge = [(0, 0)] * (n-1)
for i in range(n-1):
    a, b = map(lambda x : int(x) - 1, input().split())
    tree[a].append(b)
    tree[b].append(a)
    edge[i] = (a, b)
color_n = max(map(len, tree))

q = deque()
q.append((0, -1))

visited = set()
while q:
    i, prev_c = q.popleft()
    visited.add(i)
    c = 0
    for x in tree[i]:
        if not x in visited:
            if c == prev_c:
                c = (c + 1) % color_n
            p = (i, x) if i < x else (x, i)
            color[p] = c
            q.append((x, c))
            c = (c + 1) % color_n

print(color_n)
for e in edge:
    print(color[e] + 1)
