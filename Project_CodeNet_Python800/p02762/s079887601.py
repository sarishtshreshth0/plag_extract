
class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        elif self.rank[x] < self.rank[y]:
            x, y = y, x

        self.par[y] = x
        self.size[x] += self.size[y]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]


N, M, K = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(M)]
Y = [list(map(int, input().split())) for _ in range(K)]

friend = [[] for _ in range(N + 1)]
for a, b in X:
    friend[a].append(b)
    friend[b].append(a)

blocked = [[] for _ in range(N + 1)]
for c, d in X:
    blocked[c].append(d)
    blocked[d].append(c)

tree = UnionFind(N + 1)
for a, b in X:
    tree.unite(a, b)

ans = [0] * (N + 1)
for i in range(1, N + 1):
    ans[i] = tree.get_size(i) - len(friend[i]) - 1

for c, d in Y:
    if tree.is_same(c, d):
        ans[c] -= 1
        ans[d] -= 1

print(*ans[1:])
