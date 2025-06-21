def solve(n, m, k, a, b, c, d):
    V = range(1,n+1)
    parents = {x:x for x in V}
    def root(x):
        return x if x == parents[x] else root(parents[x])
    friends = {x:0 for x in V}
    for i in range(m):
        x, y = a[i], b[i]
        friends[x] += 1
        friends[y] += 1
        x = root(x)
        y = root(y)
        if x > y:
            x, y = y, x
        parents[y] = x
    group = {x:0 for x in V}
    for x in V:
        group[root(x)] += 1
    blocks = {x:0 for x in V}
    for i in range(k):
        x = root(c[i])
        y = root(d[i])
        if x == y:
            blocks[c[i]] += 1
            blocks[d[i]] += 1
    res = [group[root(x)] - friends[x] - blocks[x] - 1 for x in V]
    return " ".join(map(str, res))

n, m, k = map(int, input().split())
a = [0] * m
b = [0] * m
for i in range(m):
    a[i], b[i] = map(int, input().split())
c = [0] * k
d = [0] * k
for i in range(k):
    c[i], d[i] = map(int, input().split())
print(solve(n, m, k, a, b, c, d))