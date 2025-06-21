from collections import deque

N = int(input())

#頂点の色
path = [0 for _ in range(N-1)]
#木グラフ
tree = [[] for _ in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    tree[a-1].append((b-1, i))
    tree[b-1].append((a-1, i))
# print(tree)

que = deque([])
que.append((0, 0))

while que:
    v, pc = que.popleft()
    c = 1
    for nv, i in tree[v]:
        # print(f"nv{nv}, i{i}")
        if path[i] == 0:
            c = c+1 if c == pc else c
            path[i] = c
            que.append((nv, c))
            c += 1
    # print("path", path)
    # print("que", que)
print(max(path))
print(*path, sep="\n")