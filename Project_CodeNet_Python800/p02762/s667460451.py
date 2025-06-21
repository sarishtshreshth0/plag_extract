class UnionFind:
    """
    size の要素数の UnionFind を管理する
    data 中の負数の要素が根となる
    """

    def __init__(self, size):
        # 根は子を含む集合のデータ数を負数でもつ
        self.data = [-1] * size

    def merge(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y: return False

        # y の方がデータ数を多く
        if self.data[x] < self.data[y]:
            x, y = y, x

        # y に x をつなげる
        self.data[y] += self.data[x]
        self.data[x] = y
        return True

    def root(self, x):
        if self.data[x] < 0:
            return x
        self.data[x] = self.root(self.data[x])
        return self.data[x]

    def size(self, x):
        """
        根は負数でデータ数を管理しているのでそれを返す
        """
        return -self.data[self.root(x)]


N, M, K = [int(_) for _ in input().split()]
NG = [0] * (N + 1)
uf = UnionFind(N + 1)
for i in range(M):
    a, b = [int(_) for _ in input().split()]
    uf.merge(a, b)
    NG[a] += 1
    NG[b] += 1

# KG = [[] for _ in range(N + 1)]
for i in range(K):
    a, b = [int(_) for _ in input().split()]
    if uf.root(a) == uf.root(b):
        NG[a] += 1
        NG[b] += 1

res = [0] * (N)
for i in range(1, N + 1):
    cnt = uf.size(i) - NG[i] - 1
    res[i-1]=cnt
print(*res)
