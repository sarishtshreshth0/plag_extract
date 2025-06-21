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
  
n,m,k=map(int,input().split())
uf=UnionFind(n)
ab,cd=[],[]
for i in range(m):
  a,b=map(int,input().split())
  a-=1
  b-=1
  uf.union(a,b)
  ab.append((a,b))
for i in range(k):
  c,d=map(int,input().split())
  c-=1
  d-=1
  cd.append((c,d))
cnt=[]
for i in range(n):
  t=uf.count_member(i)-1
  cnt.append(t)
for a,b in ab:
  if uf.same(a,b):
    cnt[a]-=1
    cnt[b]-=1
for c,d in cd:
  if uf.same(c,d):
    cnt[c]-=1
    cnt[d]-=1
print(*cnt)
    

