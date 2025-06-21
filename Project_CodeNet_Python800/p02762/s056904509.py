# D - Friend Suggestions

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def root(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.parents[self.root(x)]

N,M,K = map(int,input().split())
friend = UnionFind(N+1)
block = [1]*(N+1)
for _ in range(M):
    x,y = map(int,input().split())
    block[x] += 1
    block[y] += 1
    friend.union(x,y)
for _ in range(K):
    x,y = map(int,input().split())
    if friend.same(x,y):
        block[x] += 1
        block[y] += 1
ans = [friend.size(i)-block[i] for i in range(1,N+1)]
print(*ans)