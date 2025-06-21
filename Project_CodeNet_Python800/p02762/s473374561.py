N, M, K = map(int, input().split())

class UnionFind:
    def __init__(self, n):
        self.ps = [-1] * (n + 1)
 
    def find(self, x):
        if self.ps[x] < 0:
            return x
        else:
            self.ps[x] = self.find(self.ps[x])
            return self.ps[x]
 
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.ps[x] > self.ps[y]:
            x, y = y, x
        self.ps[x] += self.ps[y]
        self.ps[y] = x
        return True
 
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    def size(self, x):
        x = self.find(x)
        return -self.ps[x]

uf = UnionFind(N)
friends = [0]*(N+1)
chain = [0]*(N+1)


for _ in range(M):
    A, B = map(int, input().split())
    friends[A] += 1
    friends[B] += 1
    uf.union(A, B)

for _ in range(K):
    C, D = map(int, input().split())
    if uf.same(C, D):
        friends[C] += 1
        friends[D] += 1

ans = []

for i in range(1, N+1):
    ans.append(uf.size(i) - friends[i] - 1)

print(*ans)