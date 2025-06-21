N, M, K = map(int, input().split())
ans = [0] * N
class unionfind():
  def __init__(self, N):
    self.__N = N
    self.__parent = [-1] * (N + 1)
    
  def table(self):
    print(self.__parent)
    
  def find_parent(self, x):
    if self.__parent[x] < 0:
      return x
    else:
      self.__parent[x] = self.find_parent(self.__parent[x])
      return self.__parent[x]
    
  def union(self, x, y):
    x = self.find_parent(x)
    y = self.find_parent(y)
    if x == y :
      return
    if self.__parent[x] > self.__parent[y]:
      x, y = y, x
    self.__parent[x] += self.__parent[y]
    self.__parent[y] = x
    
  def size(self, x):
    return  -self.__parent[self.find_parent(x)]
  
  def same(self, x, y):
    if self.find_parent(x) == self.find_parent(y):
      return True
    else:
      return False

uf = unionfind(N)
for _ in range(M):
  A, B = map(int, input().split())
  uf.union(A, B)
  ans[A-1] += 1
  ans[B-1] += 1

for _ in range(K):
  C, D = map(int, input().split())
  if uf.same(C, D):
    ans[C-1] += 1
    ans[D-1] += 1

for i in range(N):
  print(uf.size(i+1) - ans[i] - 1,end=" ")