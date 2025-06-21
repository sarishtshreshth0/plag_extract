class UnionFind:
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


n, m, k = map(int, input().split())
u = UnionFind(n + 1)
already = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    u.union(a, b)
    already[a] += 1
    already[b] += 1
for i in range(k):
    c, d = map(int, input().split())
    if u.same(c, d):
        already[c] += 1
        already[d] += 1

for i in range(1, n + 1):
    print(u.size(i) - already[i] - 1)
