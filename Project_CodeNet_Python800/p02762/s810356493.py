class UnionFind:
    def __init__(self, n):
        self.table = [-1] * n
 
    def _root(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self._root(self.table[x])
            return self.table[x]
 
    def count(self, x):
        return -self.table[self._root(x)]
 
    def find(self, x, y):
        return self._root(x) == self._root(y)
 
    def union(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            self.table[r1] += d2
        else:
            self.table[r1] = r2
            self.table[r2] += d1

N, M, K = map(int, input().split())
ins_friend = UnionFind(N)
friends = [0 for i in range(N)]
blocks = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    ins_friend.union(a-1, b-1)
    friends[a-1] += 1
    friends[b-1] += 1
for _ in range(K):
    c, d = map(int, input().split())
    blocks[c-1].add(d-1)
    blocks[d-1].add(c-1)
ans = [0 for i in range(N)]
for i in range(N):
    ans[i] = ins_friend.count(i) - 1 - friends[i]
    for x in blocks[i]:
        if ins_friend.find(i, x) == True:
            ans[i] -= 1
print(*ans)
