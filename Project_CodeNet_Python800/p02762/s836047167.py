import sys
import itertools
# import numpy as np
import time
import math

sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

class UnionFind(object):
    def __init__(self, n = 1):
        self.link = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.link[x] == x:
            return x

        # re-connect union find to make the height of tree lower
        # you can use while, but recursion makes it easier to reconnect
        self.link[x] = self.find(self.link[x])
        return self.link[x]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.size[x] < self.size[y]:
            x, y = y, x
        self.link[y] = x
        self.size[x] += self.size[y]
    
    def get_size(self, x):
        x = self.find(x)
        return self.size[x]

N, M, K = map(int, readline().split())
u = UnionFind(N + 1)
friends_cnt = [0 for i in range(N + 1)]
for i in range(M):
    a, b = map(int, readline().split())
    u.unite(a, b)
    friends_cnt[a] += 1
    friends_cnt[b] += 1
for i in range(K):
    c, d = map(int, readline().split())
    if u.is_same(c, d):
        friends_cnt[c] += 1
        friends_cnt[d] += 1

for i in range(1, N + 1):
    print(u.get_size(i) - friends_cnt[i] - 1)