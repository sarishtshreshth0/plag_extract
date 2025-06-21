class UnionFind1:

    def __init__(self, n):
        self.n = n
        self.par = [-1] * (n+1)

    def root(self, x):
        if self.par[x] < 0:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        if self.same(x, y):
            return
        x = self.root(x)
        y = self.root(y)
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.par[self.root(x)]


n, m = map(int, input().split())
uf = UnionFind1(n)

for _ in range(m):
    x, y, z = map(int, input().split())
    uf.unite(x, y)

cost = 0
for i in range(1, n+1):
    if uf.root(i) == i:
        cost += 1

print(cost)
