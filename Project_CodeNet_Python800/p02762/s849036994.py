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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parents[self.find(x)]

N, M, K = list(map(int, input().split()))

tree = UnionFind(N)
friends = [set() for i in range(N)]
blocks = [set() for i in range(N)]

for i in range(M):
    a, b = list(map(int, input().split()))
    friends[a-1].add(b-1)
    friends[b-1].add(a-1)
    tree.union(a-1, b-1)

for i in range(K):
    c, d = list(map(int, input().split()))
    blocks[c-1].add(d-1)
    blocks[d-1].add(c-1)

cnt = []

for i in range(N):
    group_size = tree.size(i)
    friend_cnt = len(friends[i])
    block_cnt = len([j for j in blocks[i] if tree.same(i, j)])
    cnt.append(group_size - friend_cnt - block_cnt - 1)

print(' '.join(list(map(str, cnt))))