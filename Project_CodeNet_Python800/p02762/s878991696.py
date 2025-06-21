N, M, K = map(int, input().split())
INF = 10**9
 
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
 
 
union_find = UnionFind(N)
friend_num_list = [0]*N
block_num_list = [0]*N
 
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    friend_num_list[a] += 1
    friend_num_list[b] += 1
    union_find.union(a, b)
 
for _ in range(K):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if union_find.same(c, d):
        block_num_list[c] += 1
        block_num_list[d] += 1
 
ans_list = [0]*N
for i in range(N):
    ans = union_find.size(i) - friend_num_list[i] - block_num_list[i] - 1
    ans_list[i] = ans
print(*ans_list)