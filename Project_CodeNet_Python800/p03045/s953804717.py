class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        root = x
        while self.parents[root] != root:
            root = self.parents[root]
        while self.parents[x] != root:
            parent = self.parents[x]
            self.parents[x] = root
            x = parent
        return root

    def unite(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        xrank = self.rank[xroot]
        yrank = self.rank[yroot]
        if xrank < yrank:
            self.parents[xroot] = yroot
            self.size[yroot] += self.size[xroot]
        elif xrank == yrank:
            self.parents[yroot] = xroot
            self.rank[yroot] += 1
            self.size[xroot] += self.size[yroot]
        else:
            self.parents[yroot] = xroot
            self.size[xroot] += self.size[yroot]

    def len(self, x):
        return self.size[self.find(x)]

N, M = map(int, input().split())

uf = UnionFind(N)

for _ in range(M):
    x, y, z = map(int, input().split())
    uf.unite(x - 1, y - 1)

print(len([i for i in range(N) if uf.rank[i] == 0]))