class UF():
  def __init__(self, N):
    self.parents = [-1] * N

  def find(self, n):
    if self.parents[n] < 0:
      return n
    else:
      self.parents[n] = self.find(self.parents[n])
      return self.parents[n]

  def union(self, u,v):
    p1,p2 = self.find(u),self.find(v)
    if p1==p2: return
    if p1 > p2:
      p1,p2 = p2,p1
    self.parents[p1] += self.parents[p2]
    self.parents[p2] = p1

  def same(self, u,v):
    return self.find(u) == self.find(v)

  def weight(self, u):
    p = self.find(u)
    return -self.parents[p]

N,M = map(int,input().split())

uf = UF(N+1)
for i in range(M):
  u,v,z = map(int,input().split())
  uf.union(u,v)

ans = 0
for i in range(1, N+1):
  if uf.parents[i] < 0:
    ans += 1

print(ans)