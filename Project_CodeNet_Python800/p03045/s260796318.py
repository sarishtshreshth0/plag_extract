from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter,defaultdict
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
sys.setrecursionlimit(10**6)
# INF =  float("inf")
INF = 10**18
import bisect
import statistics
mod = 10**9+7
# mod = 998244353


class UnionFind():
    # 要素0=n-1
    # parentsには親番号．根の場合は-(グループの要素数)
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # xの属するグループの根
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # xの属するグループとyの属するグループを併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # xの属するグループの要素数
    def size(self, x):
        return -self.parents[self.find(x)]

    # x,yが同じグループに属するか否か
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xの属するグループの要素からなるリスト
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    # 全グループの根からなるリスト
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    # グループ数
    def group_count(self):
        return len(self.roots())

    # {ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    # {ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書（print用）
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

class UnionFindLabel(UnionFind):
    def __init__(self, labels):
        assert len(labels) == len(set(labels))

        self.n = len(labels)
        self.parents = [-1] * self.n
        self.d = {x: i for i, x in enumerate(labels)}
        self.d_inv = {i: x for i, x in enumerate(labels)}

    def find_label(self, x):
        return self.d_inv[super().find(self.d[x])]

    def union(self, x, y):
        super().union(self.d[x], self.d[y])

    def size(self, x):
        return super().size(self.d[x])

    def same(self, x, y):
        return super().same(self.d[x], self.d[y])

    def members(self, x):
        root = self.find(self.d[x])
        return [self.d_inv[i] for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [self.d_inv[i] for i, x in enumerate(self.parents) if x < 0]


N, M = map(int, input().split())

l = [i for i in range(1, N+1)]
u = UnionFindLabel(l)

for i in range(M):
    x, y, z = map(int, input().split())

    u.union(x, y)

print(len(u.roots()))

