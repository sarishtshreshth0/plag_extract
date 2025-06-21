def main():
  import sys
  sys.setrecursionlimit(10**5+10)
  N, M, K = map(int,input().split())
  class UnionFind:
      def __init__(self, N):
          self.par = [-1 for i in range(N+1)]
          self.rank = [1]*(N+1)

      def find(self, x):
          if self.par[x] < 0:
              return x
          else:
              self.par[x] = self.find(self.par[x])
              return self.par[x]

      def same_check(self, x, y):
          return self.find(x) == self.find(y)

      def union(self, x, y):
          x = self.find(x)
          y = self.find(y)

          if self.rank[x] > self.rank[y]:
              self.par[x] += self.par[y]
              self.par[y] = x
          else:
              self.par[y] += self.par[x]
              self.par[x] = y
              if self.rank[x] == self.rank[y]:
                  self.rank[x] += 1

  UF = UnionFind(N)
  friendlist = [[] for _ in range(N+1)]
  for n in range(M):
      A, B = map(int,input().split())
      friendlist[A].append(B)
      friendlist[B].append(A)
      if not UF.same_check(A,B):
          UF.union(A, B)
  blocklist = [[] for _ in range(N+1)]
  for n in range(K):
      C, D = map(int, input().split())
      blocklist[C].append(D)
      blocklist[D].append(C)

  for person in range(1,N+1):
      root = UF.find(person)
      ans = -UF.par[root]-1
      ans -= len(friendlist[person])
      for l in blocklist[person]:
          if UF.same_check(person,l):
              ans -= 1
      print(ans)

if __name__ == '__main__':
  main()
