import sys
from collections import defaultdict, Counter, namedtuple, deque
import itertools
import functools
import bisect
import heapq
import math

MOD = 10 ** 9 + 7
# MOD = 998244353
# sys.setrecursionlimit(10**8)


class Uf:
    def __init__(self, N):
        self.p = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N

    def root(self, x):
        if self.p[x] != x:
            self.p[x] = self.root(self.p[x])

        return self.p[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        u = self.root(x)
        v = self.root(y)

        if u == v: return

        if self.rank[u] < self.rank[v]:
            self.p[u] = v
            self.size[v] += self.size[u]
            self.size[u] = 0
        else:
            self.p[v] = u
            self.size[u] += self.size[v]
            self.size[v] = 0

            if self.rank[u] == self.rank[v]:
                self.rank[u] += 1

    def count(self, x):
        return self.size[self.root(x)]


n, m, k = map(int, input().split())
friends = [[] for _ in range(n)]
block = [[] for _ in range(n)]
uf = Uf(n)
F = [list(map(int, input().split())) for _ in range(m)]
B = [list(map(int, input().split())) for _ in range(k)]

for e in F:
    friends[e[0] - 1].append(e[1] - 1)
    friends[e[1] - 1].append(e[0] - 1)
    uf.unite(e[0]-1, e[1]-1)

for e in B:
    block[e[0] - 1].append(e[1] - 1)
    block[e[1] - 1].append(e[0] - 1)

ans = [0]*n
for i in range(n):
    ans[i] = uf.size[uf.root(i)] - 1
    for f in friends[i]:
        if uf.same(i, f):
            ans[i] -= 1
    for b in block[i]:
        if uf.same(i, b):
            ans[i] -= 1

print(*ans)
