"""
UnionFind木を使う。
Ai,Aj,Zの情報が与えられたら、Ai,AjをUniteする。
同じグループにいるA同士は連鎖関係に合って、グループ内の一つでも数字がわかれば連鎖的に同グループのAの値もわかる。
この問題の問に対する答えは、グループの数となる。
"""
class UnionFind():
    def __init__(self,n):
        self.n=n
        self.parents = [i for i in range(n+1)]
        self.size = [1]*(n+1)
    def find(self,x):
        if self.parents[x]==x:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    def unite(self,x,y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        if self.size[xRoot]>self.size[yRoot]:
            self.parents[yRoot] = xRoot
            self.size[xRoot] += self.size[yRoot]
            self.size[yRoot] = 0
        else:
            self.parents[xRoot] = yRoot
            self.size[yRoot] += self.size[xRoot]
            self.size[xRoot] = 0

N,M = map(int,input().split())
tree = UnionFind(N)
for _ in range(M):
    x,y,z = map(int,input().split())
    tree.unite(x,y)
print(N-tree.size.count(0))