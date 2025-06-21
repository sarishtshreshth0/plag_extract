import sys


class UnionFind(object):
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def is_same_group(self, x, y):
        return self.find(x) == self.find(y)

    def get_group_num(self):
        return sum([1 if self.par[i] == i else 0 for i in range(len(self.par))])


N, M = map(int, sys.stdin.readline().split())
uf = UnionFind(N)
for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    x -= 1
    y -= 1
    uf.unite(x, y)

print(uf.get_group_num())
