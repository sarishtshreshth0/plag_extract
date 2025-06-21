import copy
N,M = map(int,(input().split()))
x = [0]*M
y = [0]*M
z = [0]*M
line = [[] for _ in range(N+1)]
dot = []

for i in range(M):
    x[i],y[i],z[i] = map(int,(input().split()))
    line[x[i]].append(y[i])
    dot.append(x[i])
    dot.append(y[i])

class UnionFind:

    def __init__(self, n):
        self.par =  [-1] * n
        self.rank = [0] * n
    
    def root(self,x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return
        else:
            if self.rank[x] <self.rank[y]:
                self.par[y] += self.par[x] # 負+負でsize管理 
                self.par[x] = y
            else:
                self.par[x] += self.par[y]
                self.par[y] = x
                if self.rank[x] == self.rank[y]: # 負+負でsize管理 
                    self.rank[x] += 1
    
    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.par[self.root(x)]

Tree = UnionFind(N)

for i in range(N):
    for j in line[i]:
        Tree.union(i-1,j-1)

nohint = 0
hint = []
for i in range(N):
    if Tree.size(i) == 1:
        nohint += 1
    else:
        hint.append(Tree.root(i))

print(nohint + len(set(hint)))