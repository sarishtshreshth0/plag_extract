class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = [-1]*n
        self.rank = [0]*n

    def find(self, x):
        if self.par[x-1] < 0:
            return x
        else:
            self.par[x-1] = self.find(self.par[x-1])
            return self.par[x-1]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return
        elif self.rank[x-1] > self.rank[y-1]:
            self.par[x-1] += self.par[y-1]
            self.par[y-1] = x
        else:
            self.par[y-1] += self.par[x-1]
            self.par[x-1] = y
            if self.rank[x-1] == self.rank[y-1]:
                self.rank[y-1] += 1

    def same(self, x, y):
        return self.find(x)==self.find(y)

    def count(self, x):
        return -self.par[self.find(x)-1]

from collections import deque

N,M,K=map(int,input().split())
U=UnionFind(N)
q=deque([])
for _ in range(M):
  a,b=map(int,input().split())
  U.union(a,b)
  deque.append(q,(a,b))
G=[set([]) for _ in range(N)]
for _ in range(M):
  a,b=deque.pop(q)
  if U.same(a,b):
    G[a-1].add(b)
    G[b-1].add(a)
for _ in range(K):
  a,b=map(int,input().split())
  if U.same(a,b):
    G[a-1].add(b)
    G[b-1].add(a)
ans=[0]*N
for i in range(1,N+1):
  ans[i-1]=U.count(i)-len(G[i-1])-1
print(*ans)