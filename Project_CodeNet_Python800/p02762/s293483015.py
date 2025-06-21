n, m, k = map(int, input().split())
#Union-Find
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
def unite(x, y):
    p = find(x)
    q = find(y)
    if p == q:
        return None
    if p > q:
        p,q = q,p
    par[p] += par[q]
    par[q] = p
def same(x, y):
    return find(x) == find(y)
def size(x):
    return -par[find(x)]
par = [-1 for i in range(n)]
l = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    unite(a-1, b-1)
    l[a-1] += 1
    l[b-1] += 1
for i in range(k):
    c, d = map(int, input().split())
    if same(c-1, d-1):
        l[c-1] += 1
        l[d-1] += 1
for i in range(n):
    print(size(i) - l[i] - 1, end=" ")