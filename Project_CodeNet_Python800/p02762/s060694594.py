import sys
from collections import defaultdict

# https://ikatakos.com/pot/programming_algorithm/data_structure/union_find_tree
class UnionFind:
    def __init__(self, n):
        # 負  : 根であることを示す。絶対値はランクを示す
        # 非負: 根でないことを示す。値は親を示す
        self.table = [-1] * n

    def _root(self, x):
        stack = []
        tbl = self.table
        while tbl[x] >= 0:
            stack.append(x)
            x = tbl[x]
        for y in stack:
            tbl[y] = x
        return x

    def find(self, x, y):
        return self._root(x) == self._root(y)

    def union(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        # ランクの取得
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            if d1 == d2:
                self.table[r1] -= 1
        else:
            self.table[r1] = r2

    def friend_candidate(self):
        tbl = self.table
        n = len(tbl)
        candidates = [0] * n
        root = [-1] * n
        for i, parent in enumerate(tbl):
            if parent >= 0:
                root[i] = self._root(parent)
                candidates[root[i]] += 1
        for i in range(n):
            if tbl[i] >= 0:
                candidates[i] = candidates[root[i]]
        return candidates


def main():
    input = sys.stdin.buffer.readline
    n, m, k = map(int, input().split())
    uf = UnionFind(n)
    num_friends = [0] * n
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        uf.union(a, b)
        num_friends[a] += 1
        num_friends[b] += 1
    num_block = [0] * n
    for _ in range(k):
        c, d = map(lambda x: int(x) - 1, input().split())
        if uf.find(c, d):
            num_block[c] += 1
            num_block[d] += 1
    fc = uf.friend_candidate()
    ans = [0] * n
    for i in range(n):
        ans[i] = fc[i] - num_friends[i] - num_block[i]
    print(*ans)


if __name__ == "__main__":
    main()
