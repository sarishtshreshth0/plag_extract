class UnionFind:
    def __init__(self, n):
        self.p = [-1]*n
        # union by rank
        self.r = [1]*n
 
    def find(self, x):
        if self.p[x] < 0:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]
 
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
 
        if rx != ry:
            if self.r[rx] > self.r[ry]:
                rx, ry = ry, rx
            if self.r[rx] == self.r[ry]:
                self.r[ry] += 1
            self.p[ry] += self.p[rx]
            self.p[rx] = ry
 
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    def count_member(self, x):
        return -self.p[self.find(x)]

n,m=map(int,input().split())
uf=UnionFind(n+1)
ans=n

for i in range(m):
  x,y,z=map(int,input().split())
  if not(uf.same(x,y)):
    uf.union(x,y)
    ans-=1
  uf.union(x,y)

print(ans)

