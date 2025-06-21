class UnionFind:
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

nmk = input().split()
N = int(nmk[0])
M = int(nmk[1])
K = int(nmk[2])

uf = UnionFind(N+1)
block = [0]*(N+1)

for i in range(M):
    ab = input().split()
    A = int(ab[0])
    B = int(ab[1])
    block[A]+=1
    block[B]+=1
    uf.union(A,B)

ans = [0]*(N+1)

for i in range(1,N+1):
    ans[i] = uf.size(i)-1

for i in range(K):
    cd = input().split()
    C = int(cd[0])
    D = int(cd[1])
    if uf.same(C, D):
        block[C]+=1
        block[D]+=1

for i in range(1,N+1):
    print(ans[i]-block[i])




