class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
 
    def find(self, x):#要素xが属するグループの根を返す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
 
    def union(self, x, y):#要素xが属するグループと要素yが属するグループとを併合する
        x = self.find(x)
        y = self.find(y)
 
        if x == y:
            return
 
        if self.parents[x] > self.parents[y]:
            x, y = y, x
 
        self.parents[x] += self.parents[y]
        self.parents[y] = x
 
    def size(self, x):#要素xが属するグループのサイズ（要素数）を返す
        return -self.parents[self.find(x)]
 
    def same(self, x, y):#要素x, yが同じグループに属するかどうかを返す
        return self.find(x) == self.find(y)
 
    def members(self, x):#要素xが属するグループに属する要素をリストで返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
 
    def roots(self):#すべての根の要素をリストで返す
        return [i for i, x in enumerate(self.parents) if x < 0]
 
    def group_count(self):#グループの数を返す
        return len(self.roots())
 
    def all_group_members(self):#{ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す
        return {r: self.members(r) for r in self.roots()}
 
    def __str__(self):#print()での表示用 ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
 
N, M, K = map(int, input().split())
uf = UnionFind(N)

edge1 = []
edge2 = []
for i in range(M):
    a,b = map(int,input().split())
    edge1.append((a-1,b-1))
for i in range(K):
    c,d = map(int,input().split())
    edge2.append((c-1,d-1))
for a,b in edge1:
    uf.union(a,b)

#同じグループに属する人数（自分を除く）    
ans = [uf.size(i)-1 for i in range(0,N)]

for a,b in edge1:#すでに友達なら削る
    ans[a] -= 1
    ans[b] -= 1

for c,d in edge2:
    if uf.same(c,d): #ブロック関係かつ同じグループに属しているなら
        ans[c] -= 1
        ans[d] -= 1
print(*ans)