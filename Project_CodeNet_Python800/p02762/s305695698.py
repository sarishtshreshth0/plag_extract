class UnionFind:

    def __init__(self, n):
        self.par = [-1] * n


    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x
        return True


    def root(self, x):
        path = []
        while self.par[x] >= 0:
            path.append(x)
            x = self.par[x]
        for y in path:
            self.par[y] = x
        return x


    def same(self, x, y):
        return self.root(x) == self.root(y)


    def size(self, x):
        return -self.par[self.root(x)]


n, m, k = map(int, input().split())

friends = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    friends[a].append(b)
    friends[b].append(a)

blocks = [[] for _ in range(n)]
for i in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    blocks[c].append(d)
    blocks[d].append(c)

uni = UnionFind(n)
for i, v in enumerate(friends):
    for j in v:
        uni.unite(i, j)

for i in range(n):
    ans = uni.size(i) - len(friends[i]) - 1
    for block in blocks[i]:
        if uni.same(i, block):
            ans -= 1
    print(ans, end=' ')