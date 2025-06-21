def main():
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

        def other_members(self, x):
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root and i != x]

        def roots(self):
            return [i for i, x in enumerate(self.parents) if x < 0]

        def __str__(self):
            return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    import sys
    def input():
        return sys.stdin.readline().rstrip()
    n, m, k = list(map(int, input().split()))
    uf = UnionFind(n)
    counts = [0] * n
    for _ in range(m):
        a, b = list(map(lambda x: int(x) - 1, input().split()))
        uf.union(a, b)
        counts[a] += 1
        counts[b] += 1
    for _ in range(k):
        c, d = list(map(lambda x: int(x) - 1, input().split()))
        if uf.same(c, d):
            counts[c] += 1
            counts[d] += 1
    print(' '.join([str(uf.size(i) - counts[i] - 1) for i in range(n)]))

if __name__ == '__main__':
    main()
