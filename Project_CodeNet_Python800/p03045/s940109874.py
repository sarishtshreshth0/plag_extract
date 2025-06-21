class UnionFindTree:
    def __init__(self, n):
        self.par = [-1 for _ in range(n)]
        
    def find(self, x):
        if self.par[x] < 0:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]
        
    def size(self, x):
        return -self.par[self.find(x)]
        
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 0
        if self.size(x) < self.size(y):
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x
        return 1
        
n, m = map(int, input().split())
uf = UnionFindTree(n)
ans = n
for _ in range(m):
    x, y, z = map(int, input().split())
    ans -= uf.unite(x-1, y-1)
print(ans)