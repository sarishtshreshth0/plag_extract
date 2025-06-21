N, M, K = map(int, input().split())

class UnionFind:
    def __init__(self, n):
        self.table = [-1 for _ in range(n)]
        self.size = [1]*n

    def _root(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self._root(self.table[x])
            return self.table[x]

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
            self.size[r1] += self.size[r2]
            if d1 == d2:
                self.table[r1] -= 1
        else:
            self.table[r1] = r2
            self.size[r2] += self.size[r1]

    def group_size(self, x):
        return self.size[self._root(x)]

Friends = [list(map(int, input().split())) for _ in range(M)]
Blocks = [list(map(int, input().split())) for _ in range(K)]

Friendship = UnionFind(N)
Cant = [0]*N

for a in Friends:
    Friendship.union(a[0]-1, a[1]-1)

for b in Friends:
    if Friendship.find(b[0]-1, b[1]-1):
        Cant[b[0]-1] += 1; Cant[b[1]-1] += 1

for c in Blocks:
    if Friendship.find(c[0]-1, c[1]-1):
        Cant[c[0]-1] += 1; Cant[c[1]-1] += 1

print(*[Friendship.group_size(i)-Cant[i]-1 for i in range(N)])