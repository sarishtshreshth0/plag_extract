import sys

# import re
# import math
# import collections
# import decimal
# import bisect
# import itertools
# import fractions
# import functools
# import copy
# import heapq
# import decimal
# import statistics
# import queue

sys.setrecursionlimit(10000001)
INF = 10 ** 10
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    n, m, k = ns()

    friend = UnionFind(n)

    myfriend = [0 for _ in range(n)]
    blocks = {}
    for i in range(n):
        blocks[i] = set()

    for _ in range(m):
        ai, bi = ns()
        ai -= 1
        bi -= 1
        friend.union(ai, bi)
        myfriend[ai] += 1
        myfriend[bi] += 1

    for _ in range(k):
        ci, di = ns()
        ci -= 1
        di -= 1

        blocks[ci].add(di)
        blocks[di].add(ci)

    tmp = 0
    for i in range(n):
        tmp_block = 0
        for j in blocks[i]:
            if friend.same(i, j):
                tmp_block += 1

        ans = friend.size(i) - 1 - myfriend[i] - tmp_block
        print(ans)


if __name__ == '__main__':
    main()
