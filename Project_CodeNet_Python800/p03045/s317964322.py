N, M = map(int, input().split())
tree = [-1 for i in range(N)]

def root(x):
    if tree[x] < 0:
        return x
    tree[x] = root(tree[x])
    return tree[x]
def find(x, y):
    return root(x) == root(y)
def union(x, y):
    x = root(x)
    y = root(y)
    if x != y:
        if tree[x] < tree[y]:
            x, y = y, x
        tree[x] += tree[y]
        tree[y] = x
        return 1
    return 0

cnt = 0
for i in range(M):
    x, y, z = map(int, input().split())
    cnt += union(x - 1, y - 1)
print(N - cnt)