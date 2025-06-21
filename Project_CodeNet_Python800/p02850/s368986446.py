import collections

n = int(input())
graph = [tuple(map(int, input().split())) for _ in range(n - 1)]
tree = [[] for _ in range(n)]
deg = [0] * n
color = {}
for a, b in graph:
    a, b = min(a - 1, b - 1), max(a - 1, b - 1)
    deg[a] += 1
    deg[b] += 1
    tree[a].append(b)
    tree[b].append(a)
    color[(a, b)] = 0
color_max = max(deg)
print(color_max)

c = [0] * n
c[0] = -1
que = collections.deque([0])
while len(que) != 0:
    i = que.popleft()
    tmp = 1
    for j in tree[i]:
        if c[j] != 0: continue
        a, b = min(i, j), max(i, j)
        if tmp == c[i]: tmp += 1
        color[(a, b)] = tmp
        c[j] = tmp
        que.append(j)
        tmp += 1

for a, b in graph:
    a, b = min(a - 1, b - 1), max(a - 1, b - 1)
    print(color[(a, b)])
