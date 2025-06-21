class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
        
    def union(self, x, y):
        xx = self.find(x)
        yy = self.find(y)
        if self.rank[xx] < self.rank[yy]:
            self.par[xx] = yy
        else:
            self.par[yy] = xx
            if self.rank[xx] == self.rank[yy]:
                self.rank[xx] += 1
        self.par[x] = self.find(x)
        self.par[y] = self.find(y)
                
    def same_check(self, x, y):
        return self.find(x) == self.find(y)
    
n, m = map(int, input().split())
union = UnionFind(n)

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    union.union(a, b)

for i in range(n):
    union.find(i)
print(len(set(union.par)))