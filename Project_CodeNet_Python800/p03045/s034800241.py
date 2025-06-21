import collections
# from collections import deque
# from fractions import gcd # >=Python3.5 # lcm = (a*b)//gcd(a,b)
# from math import gcd # <Python3.5
# from math import sqrt

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

n,m = map(int,input().split())
uf = UnionFind(n)

for i in range(m):
    x,y,z = map(int,input().split())
    uf.union(x,y)

# cnt = collections.Counter(uf.par)

# print(cnt)

# print(len(set(cnt))-1)

tank = set([])
for i in range(1,n+1):
    tank.add(uf.find(i))
print(len(tank))