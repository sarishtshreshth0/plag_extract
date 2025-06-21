
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

N, M, K = map(int,input().split())
uf = UnionFind(N)
f_b = [set() for _ in range(N)]
ans = []
for i in range(M):
    A, B = map(int,input().split())
    A -= 1
    B -= 1
    uf.union(A, B)
    f_b[A].add(B)
    f_b[B].add(A)
    
for i in range(K):
    C, D = map(int,input().split())
    C -= 1
    D -= 1
    if uf.same(C, D):
        f_b[C].add(D)
        f_b[D].add(C)    

for i in range(N):
    ans.append(uf.size(i) - len(f_b[i]) - 1)
print(*ans)