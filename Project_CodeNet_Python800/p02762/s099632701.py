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

N, M, K = map(int, input().split())
friends_uf = UnionFind(N)
counts = [1] * N
for _ in range(M):
    i, j = map(lambda n: int(n) - 1, input().split())
    counts[i] += 1
    counts[j] += 1
    friends_uf.union(i, j)
blocks_graph = [[] for _ in range(N)]
for _ in range(K):
    i, j = map(lambda n: int(n) - 1, input().split())
    blocks_graph[i].append(j)
    blocks_graph[j].append(i)
for i in range(N):
    ans = friends_uf.size(i) - counts[i]
    for j in blocks_graph[i]:
        if friends_uf.same(i, j):
            ans -= 1
    print(ans, end=" ")