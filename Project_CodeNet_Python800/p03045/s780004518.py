from collections import deque
n, m = map(int, input().split())
#z:oddなら a_x, a_y の一方が1、もう一方が２
#z:evenなら a_x, a_yがどちらも２またはどちらも１
edges = [[]*n for _ in range(n)]
for i in range(m):
    x, y, z = map(int, input().split())
    edges[x-1].append(y-1)
    edges[y-1].append(x-1)

d = deque()
id_list = [-1]*n


def dfs(start, id):
    d.append(start)
    id_list[start] = id
    while d:
        p = d.pop()
        for c in edges[p]:
            if id_list[c] != -1:
                continue
            id_list[c] = id
            d.append(c)

id = 1
for i in range(n):
    if id_list[i] == -1:
        dfs(i, id)
        id += 1

print(max(id_list))