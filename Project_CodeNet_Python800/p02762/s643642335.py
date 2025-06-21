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


################################
N, M, K = map(int, input().split())
uf = UnionFind(N + 1)
friends = [set() for _ in range(N + 1)]
blocks = [set() for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].add(b)
    friends[b].add(a)
    uf.union(a, b)

for _ in range(K):
    c, d = map(int, input().split())
    blocks[c].add(d)
    blocks[d].add(c)

ans = []

for i in range(1, N + 1):
    group_size = uf.size(i)
    friend_cnt = len(friends[i])
    block_cnt = 0
    for j in blocks[i]:
        if uf.same(i, j):
            block_cnt += 1
    suggest_cnt = group_size - friend_cnt - block_cnt - 1
    ans.append(suggest_cnt)

print(*ans)
