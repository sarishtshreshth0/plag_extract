import sys
input = sys.stdin.readline

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):                                          # 根を見つける関数を定義（同時にxを直接根にくっつける操作も行う）
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])        # 右辺で再帰的に根を探索。根に到達すると一つ目のif判定に引っかかるので、
                                                                # 最終的にself.parents[根]が返ってくる。
                                                                # これを左辺に代入することで、根が親になるように変更する。（根までの距離が長いとO(N)になってしまうので）
            return self.parents[x]

    def union(self, x, y):                                      # 二つの木をくっつける（子を多く持つ方を根とした親子関係）。これは破壊的操作を行う。
        x = self.find(x)                                        # xをxの根に置き換える
        y = self.find(y)                                        # yをyの根に置き換える

        if x == y:                                              # 根が同じなら置き換える必要なし
            return

        if self.parents[x] > self.parents[y]:                   # 子がたくさんある方を x とする（出来るだけ浅い木にするため）
            x, y = y, x

        self.parents[x] += self.parents[y]                      # xの子の数を更新
        self.parents[y] = x                                     # yの親を更新

    def same(self, x, y):                                       # xとyが同じ根の子かを判定
        return self.find(x) == self.find(y)

    def size(self, x):                                          # xの根のparent（= 要素数）を返す
        return -self.parents[self.find(x)]

    def members(self, x):                                       # xが属するグループの要素をリストとして返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):                                            # 全ての根の要素をリストとして返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):                                      # グループの数を返す
        return len(self.roots())

    def all_group_members(self):                                # {根:[根の子のリスト],...}を辞書で返す
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):                                          # print(self) での返し方を定義
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


##############################################################################################################

V, E, K = map(int, input().split())                            # V: 頂点数　E: 辺の数

tree = UnionFind(V)

edges = [[] for _ in range(V)]
for _ in range(E):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree.union(a, b)
    edges[a].append(b)
    edges[b].append(a)


blocks = [[] for _ in range(V)]
for _ in range(K):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    blocks[a].append(b)
    blocks[b].append(a)

res = []
for x in range(V):
    n = tree.size(x)
    temp = n-1
    for y in edges[x]:
        if tree.same(x,y):
            temp -= 1
    for y in blocks[x]:
        if tree.same(x,y):
            temp -= 1
    res.append(temp)

print(*res)