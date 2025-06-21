n, m = map(int, input().split())
tree = [-i for i in range(n+1)]
rank = [1 for _i in range(n+1)]
def search_root(num, tree=tree):
    if tree[num] < 0:
        return num
    else:
        tree[num] = search_root(tree[num])
        return tree[num]

for _i in range(m):
    x, y, z = map(int, input().split())
    x, y = [search_root(x), search_root(y)]
    if x==y:
        continue
    else:
        if rank[x]<rank[y]:
            rank[y] += 1
            tree[x] = y
        else:
            rank[x] += 1
            tree[y] = x
print(sum(1 for i in tree if i<0))