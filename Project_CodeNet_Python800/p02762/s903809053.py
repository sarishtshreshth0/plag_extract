# -*- coding: utf-8 -*-

class UnionFind():
  def __init__(self, n):
    self.n = n                           # 要素数
    self.parents = [i for i in range(n)] # 要素の親
    self.rank = [0] * n                  # 木の深さ
    self.size = [1] * n                  # iを根とする集合の要素数

  def find(self, x):
    if self.parents[x] == x:
      return x
    else:
      # 経路圧縮
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]
    
  def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)
    
    if root_x != root_y:
      # 深さが小さい方を大きい方に併合する
      if self.rank[root_x] > self.rank[root_y]:
        self.parents[root_y] = root_x
        self.size[root_x] += self.size[root_y]
      else:
        self.parents[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        if self.rank[root_x] == self.rank[root_y]:
          self.rank[root_y] += 1

N, M, K = map(int, input().split())
A = list()
B = list()
C = list()
D = list()
union_find = UnionFind(n=N)
direct_and_block_count = [0] * N
ans = ''
for i in range(M):
  a, b = map(int, input().split())
  A.append(a-1)
  B.append(b-1)
  union_find.union(a-1, b-1)
  direct_and_block_count[a-1] += 1
  direct_and_block_count[b-1] += 1
for i in range(K):
  c, d = map(int, input().split())
  C.append(c-1)
  D.append(d-1)
  if union_find.find(c-1) == union_find.find(d-1):
    # 同じ集合の場合
    direct_and_block_count[c-1] += 1
    direct_and_block_count[d-1] += 1

ans = [0] * N
for i in range(N):
  # 直接の友達、ブロック、自分自身を除く
  ans[i] = union_find.size[union_find.find(i)] - direct_and_block_count[i] - 1
print(*ans)