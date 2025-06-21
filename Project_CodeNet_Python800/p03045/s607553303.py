class Union_Find:
  def __init__(self,n=0):
    self.vertices=n
    self.mother=[-1 for i in range(self.vertices)]
    self.size_temp=[1 for i in range(self.vertices)]
  
  def root(self,x):
    normalize_v=[]
    while x!=-1:
      normalize_v.append(x)
      y=x
      x=self.mother[x]
    for i in normalize_v[:-1]:
      self.mother[i]=y
    return y
  
  def union(self,x,y):
    root_x=self.root(x)
    root_y=self.root(y)
    if root_x!=root_y:
      self.mother[root_x]=root_y
      self.size_temp[root_y]+=self.size_temp[root_x]
  
  def find(self,x,y):
    if self.root(x)==self.root(y):
      return True
    else:
      return False
  
  def size(self,x):
    return self.size_temp[self.root(x)]


n,m=map(int,input().split())
uf=Union_Find(n)
for i in range(m):
  x,y,z=map(int,input().split())
  x-=1
  y-=1
  uf.union(x,y)

c=0
for i in range(n):
  c+=i==uf.root(i)
print(c)