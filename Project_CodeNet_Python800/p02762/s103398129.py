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
uf = UnionFind(n)
friend = [set([]) for i in range(n)]
for i in range(m):
    ai, bi = map(int, input().split())
    ai -= 1; bi -= 1
    uf.union(ai, bi)
    friend[ai].add(bi)
    friend[bi].add(ai)

block = [set([]) for i in range(n)]
for i in range(k):
    ci, di = map(int, input().split())
    ci -= 1; di -= 1
    block[ci].add(di)
    block[di].add(ci)

for i in range(n):
    uf.find(i)

ans = []
for i in range(n):
    num = uf.size(i) - len(friend[i]) - 1
    for j in block[i]:
        if uf.find(i) == uf.find(j):
            num -= 1
    ans.append(num)

print(' '.join(map(str, ans)))