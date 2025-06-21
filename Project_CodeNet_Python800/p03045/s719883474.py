class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.rank = [1] * n
        self.count = [1] * n

    def get_root(self, i):
        while self.parent[i] != -1:
            i = self.parent[i]
        return i

    def is_same_tree(self, i, j):
        return self.get_root(i) == self.get_root(j)

    def merge(self, i, j):
        i = self.get_root(i)
        j = self.get_root(j)
        if i == j:
            return

        if self.rank[i] > self.rank[j]:
            self.parent[j] = i
            self.rank[i] = max(self.rank[i], self.rank[j] + 1)
            self.count[i] += self.count[j]
        else:
            self.parent[i] = j
            self.rank[j] = max(self.rank[j], self.rank[i] + 1)
            self.count[j] += self.count[i]

n, m = [int(i) for i in input().split()]
uf = UnionFind(n)
for _ in range(m):
    x, y, _ = [int(i) - 1 for i in input().split()]
    uf.merge(x, y)
print(uf.parent.count(-1))