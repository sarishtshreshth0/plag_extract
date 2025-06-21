class UnionFind:
    def __init__(self,n):
        self.n=n
        self.parent=[i for i in range(n)]
        self.rank=[1]*n#木の高さ
        self.size=[1]*n#size[i]はiを根とするグループのサイズ

    def find(self,x):#ｘの根（親）を返す
        if self.parent[x]==x:
            return x
        else:
            self.parent[x]=self.find(self.parent[x])#経路圧縮
            return self.parent[x]

    def unite(self,x,y):#ｘ、ｙの集合の統合
        x=self.find(x)
        y=self.find(y)
        if x!=y:
            if self.rank[x]<self.rank[y]:#ランクの比較
                self.parent[x]=y
                self.size[y]+=self.size[x]
            else:
                self.parent[y]=x
                self.size[x]+=self.size[y]
                if self.rank[x]==self.rank[y]:
                    self.rank[x]+=1
    def group_size(self,x):#ｘが属する集合の大きさ
        return self.size[self.find(x)]
    def is_same(self,x,y):#ｘ、ｙが同じ集合に属するかを判定する
        return self.find(x)==self.find(y)

n,m,k=map(int,input().split())

uf=UnionFind(n)
ans = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    uf.unite(a-1,b-1)
    ans[a - 1] -= 1
    ans[b - 1] -= 1
for i in range(k):
    c, d = map(int, input().split())
    if uf.is_same(c-1,d-1):
        ans[c-1]-=1
        ans[d-1]-=1

for i in range(n):
    ans[i]+=uf.group_size(i)-1
    print(ans[i])
