import sys


class UnionFind:
    def __init__(self, n):
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
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            self.table[r1] += d2
        else:
            self.table[r1] = r2
            self.table[r2] += d1


def main():
    n, m, k = map(int, sys.stdin.buffer.readline().split())
    uf = UnionFind(n)
    fb = [0]*n
    i = 0
    for x in sys.stdin.buffer.readlines():
        if i < m:
            a, b = map(int, x.split())
            fb[a-1] += 1
            fb[b-1] += 1
            uf.union(a-1, b-1)
        else:
            c, d = map(int, x.split())
            if uf._root(c-1) == uf._root(d-1):
                fb[c-1] += 1
                fb[d-1] += 1
        i += 1

    ans = [-uf.table[uf._root(i)]-1-fb[i] for i in range(n)]
    print(*ans)


if __name__ == "__main__":
    main()
