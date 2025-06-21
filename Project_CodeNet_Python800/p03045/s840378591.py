class UnionFind:
    def __init__(self, n):
        self.parent = [ -1 for _ in range(n) ]
        self._size = n
    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x != y:
            if self.parent[y] < self.parent[x]:
                x, y = y, x
            self.parent[x] += self.parent[y]
            self.parent[y] = x
            self._size -= 1
    def same(self, x, y):
        return self.root(x) == self.root(y)
    def root(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]
    def size(self, x):
        return -self.parent[self.find(x)]

n, m = map(int, input().split())
tree = UnionFind(n)

for i in range(m):
    x, y, z = map(int, input().split())
    x -= 1; y -= 1;
    tree.unite(x, y)

print(tree._size)