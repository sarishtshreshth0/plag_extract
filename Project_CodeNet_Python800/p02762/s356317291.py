N, M, K = map(int, input().split())
F = [[] for _ in range(N)]
B = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    F[a].append(b)
    F[b].append(a)

for _ in range(K):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    B[c].append(d)
    B[d].append(c)


class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納。par[x] == xの時そのノードは根(最初は全て根)
        self.par = [i for i in range(n)]
        # 木の高さを格納する（初期状態では0）
        self.rank = [0] * n
        # 人間の数
        self.size = [1] * n

    # 検索
    def find(self, x):
        # 根ならその番号を返す
        if self.par[x] == x:
            return x
        # 根でないなら、親の要素で再検索
        else:
            # 走査していく過程で親を書き換える(return xが代入される)
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        # 根を探す
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        # 木の高さを比較し、低いほうから高いほうに辺を張る
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            # 木の高さが同じなら片方を1増やす
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # すべての頂点に対して親を検索する
    def all_find(self):
        for n in range(len(self.par)):
            self.find(n)


UF = UnionFind(N)
for iam in range(N):
    for friend in F[iam]: 
        UF.union(iam, friend) # 自分と自分の友達を併合

ans = [UF.size[UF.find(iam)] - 1 for iam in range(N)] # 同じ集合に属する人の数

for iam in range(N):
    ans[iam] -= len(F[iam]) # すでに友達関係にある人達を引く

for iam in range(N):
    for block in B[iam]:
        if UF.same(iam, block): # ブロック関係にあったら引く
            ans[iam] -= 1

print(*ans, sep=' ')
