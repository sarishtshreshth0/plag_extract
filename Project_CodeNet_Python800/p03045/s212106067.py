class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rnk = [0] * (n + 1)

    def Find_Root(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        if x == y:
            return
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1


import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n, m = map(int, input().split())
u = UnionFind(n)
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    u.Unite(a, b)
print(len(set(u.Find_Root(i) for i in range(n))))
