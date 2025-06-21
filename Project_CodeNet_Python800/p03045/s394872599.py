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
            return 0
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

N,M,*f = map(int, open(0).read().split())
XYZ = [f[i:i+3] for i in range(0, len(f), 3)]
XY = [(x[0],x[1]) for x in XYZ]
uf = UnionFind(N)
ans = 0
for x, y in XY:
    uf.union(x-1,y-1)
for x in uf.parents:
    if x < 0:
        ans += 1
print(ans)