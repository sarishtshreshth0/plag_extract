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

N, M, K = map(int, input().split())
Network = UnionFind(N)
Friend = [0] * N  #人indexの友達の数
BlockInNetwork = [0] * N  #同じグループの中でブロックされている人の数

for _ in range(M):  #友達関係
    a, b = map(int, input().split())
    Network.union(a-1, b-1)
    Friend[a-1] += 1
    Friend[b-1] +=1

for _ in range(K): #ブロック関係
    c, d = map(int, input().split())
    if Network.same(c-1, d-1):  #same=aとbが同じグループか True or False
        BlockInNetwork[c-1] += 1
        BlockInNetwork[d-1] += 1

out = [0] * N  #友達候補の数 = そのグループの数 - 直の友達の数 - ブロックされている人の数 - 自分
for i in range(N):
    out[i] = Network.size(i) - Friend[i] - BlockInNetwork[i] - 1
print(*out)

