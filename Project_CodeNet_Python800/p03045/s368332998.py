n, m = map(int, input().split())
tree = [-i for i in range(n+1)]

for _i in range(m):
    x, y, z = map(int, input().split())
    while tree[x]>0:
        x = tree[x]
    while tree[y]>0:
        y = tree[y]
    x, y = sorted([x, y])
    if x==y:
        continue
    else:
        tree[y] = x
print(sum(1 for i in tree if i<0))