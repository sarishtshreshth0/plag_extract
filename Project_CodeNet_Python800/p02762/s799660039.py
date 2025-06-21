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

N,M,K = map(int,input().split())
tree = UnionFind(N)
friends = [list(map(int,input().split())) for _ in range(M)]
blocks = [list(map(int,input().split())) for _ in range(K)]
for a,b in friends:
    tree.unite(a,b)
for a,b in friends:
    tree.unite(a,b)

ans = [tree.size[tree.parents[i]]-1 for i in range(N+1)]
for a,b in friends:
    ans[a] -= 1
    ans[b] -= 1

for a,b in blocks:
    if tree.parents[a] == tree.parents[b]:
        ans[a] -= 1
        ans[b] -= 1

ans = [str(ans[i]) for i in range(1,N+1)]
print(" ".join(ans))

