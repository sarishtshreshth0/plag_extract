class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

n, m, k = map(int, input().split())
uf = UnionFind(n+1)
n_rlts = [0]*(n+1)
for i in range(m):
    a,b = map(int, input().split())
    n_rlts[a] += 1
    n_rlts[b] += 1
    uf.union(a,b)
for i in range(k):
    c,d = map(int, input().split())
    if uf.same(c,d):
        n_rlts[c] += 1
        n_rlts[d] += 1
res = ""
for i in range(1,n+1):
    res += str(uf.size(i)-1-n_rlts[i]) + " "
print(res[:-1])