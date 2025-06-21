class UnionFind():
    
    # 要素数を指定して作成 はじめは全ての要素が別グループに属し、親はいない
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    
    # xの根を返す
    def find(self, x):
        if self.parents[x] < 0:  return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    # xとyが属するグループを併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:  return
        if self.parents[x] > self.parents[y]:  x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    # xが属するグループの要素数
    def size(self, x):  return -self.parents[self.find(x)]
    
    # ｘとyが同じグループか否か
    def same(self, x, y):  return self.find(x) == self.find(y)
    
    # xと同じメンバーの要素
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    # 根の一覧
    def roots(self):  return [i for i, x in enumerate(self.parents) if x < 0]
    
    # グループ数
    def group_count(self):  return len(self.roots())
    
    # 可視化 [print(uf)]
    def __str__(self):  return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

N, M, K = list(map(int,input().split()))

G1 = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G1[a - 1].append(b - 1)
    G1[b - 1].append(a - 1)

G2 = [[] for _ in range(N)]
for i in range(K):
    a, b = map(int, input().split())
    G2[a - 1].append(b - 1)
    G2[b - 1].append(a - 1)
    
uf = UnionFind(N)
for i in range(N):
    for j in G1[i]:
        uf.union(i, j)
    
for i in range(N):
    ans = uf.size(i)  - len(G1[i]) - 1
    for j in G2[i]:
        if uf.same(i, j):  ans -= 1
    print(ans)