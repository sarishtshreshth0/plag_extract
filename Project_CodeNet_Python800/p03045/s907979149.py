from sys import setrecursionlimit
#setrecursionlimit(10**5)
class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納
        # par[x]=xの時そのノードは根　
        self.par = [i for i in range(n)]
        # rank
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        # 根の番号を返す(所属する集合を確認する)
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def check(self, x, y):
        # x,yが同じ集合に属するかどうか調べる
        return self.find(x) == self.find(y)


    def union(self, x, y):
        # 根を探す
        x = self.find(x)
        y = self.find(y)
        if x == y:return
        # rankの小さいものを大きいほうにくっつける
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def count_group(self):
        return len({self.find(x) for x in range(n)})

n, m = map(int,input().split())

uf = UnionFind(n)
for i in range(m):
    x, y, z = map(int,input().split())
    uf.union(x - 1, y - 1)

print(uf.count_group())