class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納。ノード番号は１から開始なのでn+1個。
        # par[x]<0の時そのノードは根で、par[x]の絶対値はグループのサイズ
        self.parents = [-1] * (n+1)

    # 親の親の...を辿って根を見つける
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            # 再度検索する時に手間がかからないよう根を繋ぎかえる
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # xの属するグループとyの属するグループを併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True

    # 同じ集合に属するか判定
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xが属するグループのサイズを返す
    def size(self, x):
        x = self.find(x)
        return -self.parents[x]

n, m, k = map(int, input().split())
friend = [list(map(int, input().split())) for _ in range(m)]
block = [list(map(int, input().split())) for _ in range(k)]

already = [0]*n
uf = UnionFind(n)

for a, b in friend:
    uf.union(a, b)
    already[a-1] += 1
    already[b-1] += 1

ans = [uf.size(x) - already[x-1] - 1 for x in range(1, n+1)]

for a, b in block:
    if uf.same(a, b):
        ans[a-1] -= 1
        ans[b-1] -= 1

print(*ans)