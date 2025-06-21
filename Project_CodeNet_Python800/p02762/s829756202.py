class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n
    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)


N,M,K = map(int,input().split())

Friend = [[] for _ in range(N)]
Block  = [[] for _ in range(N)]

for _ in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    Friend[a].append(b)
    Friend[b].append(a)

for _ in range(K):
    c,d = map(int,input().split())
    c-=1
    d-=1
    Block[c].append(d)
    Block[d].append(c)

UF = UnionFind(N)

for i in range(N):
    for friend in Friend[i]:
        UF.union(i,friend)

li = [0]*N
for i in range(N):
    li[i] += (UF.size[UF.find(i)]-1-len(Friend[i]))


for i in range(N):
    for block in Block[i]:
        if UF.same_check(block,i):
            li[i]-=1
         
print(*li) 