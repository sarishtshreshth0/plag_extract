import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


class UnionFind:
    def __init__(self, n):
        self.p = [-1]*n
        self.r = [1]*n

    def find(self, x):
        if self.p[x] < 0:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.r[rx] > self.r[ry]:
                rx, ry = ry, rx
            if self.r[rx] == self.r[ry]:
                self.r[ry] += 1
            self.p[ry] += self.p[rx]
            self.p[rx] = ry

    def count_roots(self):
        return sum(p < 0 for p in self.p)


n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    x, y, _ = map(lambda x: int(x)-1, input().split())
    uf.union(x, y)
print(uf.count_roots())
