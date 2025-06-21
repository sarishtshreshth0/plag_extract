class UnionFind:
    def __init__(self, n):
        self.ps = [-1] * (n + 1)

    def find(self, x):
        if self.ps[x] < 0:
            return x
        else:
            self.ps[x] = self.find(self.ps[x])
            return self.ps[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.ps[x] > self.ps[y]:
            x, y = y, x
        self.ps[x] += self.ps[y]
        self.ps[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        x = self.find(x)
        return -self.ps[x]


n, m, k = map(int, input().split())


uf = UnionFind(n)

friends = [0] * (n + 1)
chain = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    friends[a] += 1
    friends[b] += 1
    uf.union(a, b)

for _ in range(k):
    c, d = map(int, input().split())
    if uf.same(c, d):
        friends[c] += 1
        friends[d] += 1

ans = []
for i in range(1, n + 1):
    ans.append(uf.size(i) - friends[i] - 1)

print(*ans)