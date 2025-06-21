class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1 for _ in range(n)]

    def root(self, x):
        '''
        xの根を返す
        '''
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        '''
        二つの木を合併する
        '''
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def size(self, x):
        '''
        xが属する木のサイズを返す
        '''
        return -self.parents[self.root(x)]

    def same(self, x, y):
        '''
        xとyが同じ木に属するかを調べる
        '''
        return self.root(x) == self.root(y)

    def members(self, x):
        '''
        xの木のリストを返す
        '''
        root = self.root(x)
        return [i for i in range(self.n) if self.root(i) == root]

    def roots(self):
        '''
        全ての根のリストを返す
        '''
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        '''
        木の数を返す
        '''
        return len(self.roots())

    def all_group_members(self):
        '''
        木の辞書を返す
        '''
        return {r:  self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

N, M, K = map(int, input().split())
if M:
    AB = [map(int, input().split()) for _ in range(M)]
    A, B = [list(i) for i in zip(*AB)]
if K:
    CD = [map(int, input().split()) for _ in range(K)]
    C, D = [list(i) for i in zip(*CD)]


friend = [[] for i in range(N)]
block = [[] for i in range(N)]

uf = UnionFind(N)

if M:
    for i in range(M):
        uf.union(A[i]-1, B[i]-1)
        friend[A[i]-1].append(B[i]-1)
        friend[B[i]-1].append(A[i]-1)

if K:
    for i in range(K):
        block[C[i]-1].append(D[i]-1)
        block[D[i]-1].append(C[i]-1)

for i in range(N):
    tmp = uf.size(i)-1
    for v in friend[i]:
        if uf.same(i, v):
            tmp -= 1
    for v in block[i]:
        if uf.same(i, v):
            tmp -= 1

    print(tmp)