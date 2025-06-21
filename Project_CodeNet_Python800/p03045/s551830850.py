N,M=map(int,input().split())
XYZ=[]
for i in range(M):
  x,y,z=map(int,input().split())
  XYZ.append([x,y,z])
class UnionFind():
  def __init__(self,n):
    self.n=n
    self.root=[-1]*(n+1)
    self.rnk=[0]*(n+1)
  def find(self,x):
    if self.root[x]<0:
      return x
    else:
      self.root[x]=self.find(self.root[x])
      return self.root[x]
  def unite(self,x,y):
    x=self.find(x)
    y=self.find(y)
    if x==y:
      return
    elif self.rnk[x]>self.rnk[y]:
      self.root[x]+=self.root[y]
      self.root[y]=x
    else:
      self.root[y]+=self.root[x]
      self.root[x]=y
      if self.rnk[x]==self.rnk[y]:
        self.rnk[y]+=1
  def count(self,x):
    return -self.root[self.find(x)]
uf=UnionFind(N)
for i in range(M):
  uf.unite(XYZ[i][0],XYZ[i][1])
ans=-1
for i in range(len(uf.root)):
  if uf.root[i]<0:
    ans+=1
print(ans)