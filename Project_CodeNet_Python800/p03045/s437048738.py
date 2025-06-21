# https://atcoder.jp/contests/abc126/tasks/abc126_e

######### Union Find ########
class UnionFind(object):
    def __init__(self, n):
        self.n = n
        self.root = [-1] * n
        self.rnk = [0] * n

    def find(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def count(self, x):
        return -self.root[self.find(x)]

if __name__ == '__main__':
    n, m = map(int, input().split())
    uf = UnionFind(n)

    for _ in range(m):
        xi, yi, zi = map(int, input().split())
        xi -= 1
        yi -= 1
        uf.unite(xi, yi)

    count = 0
    for i in range(n):
        if uf.root[i] < 0:
            count += 1
    print(count)
