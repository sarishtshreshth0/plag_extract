class UnionFind():
    def __init__(self, n):
        self.parents = [-1]*n
        self.rank = [0]*n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            return self.find(self.parents[x])

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


N, M = list(map(int, input().split()))
uf = UnionFind(N)
for _ in range(M):
    x, y, z = list(map(int, input().split()))
    x -= 1
    y -= 1
    uf.union(x, y)

ct = 0
for i in range(N):
    if uf.parents[i] < 0:
        ct += 1
print(ct)
