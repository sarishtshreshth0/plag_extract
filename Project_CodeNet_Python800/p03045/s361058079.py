import sys
input = lambda: sys.stdin.readline()


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x


n, m = map(int, input().split())
uf = UnionFind(n)

for _ in range(m):
    a, b, z = map(int, input().split())
    uf.unite(a - 1, b - 1)

cnt = 0
for x in uf.par:
    cnt += 1 if x < 0 else 0
print(cnt)
