class UnionFind():
    def __init__(self, n):
        self._n = n
        self._table = [-1]*n

    def _root(self, x):
        stack = []
        while self._table[x] >= 0:
            stack.append(x)
            x = self._table[x]
        for y in stack:
            self._table[y] = x
        return x
    
    def unite(self, x, y):
        x, y = self._root(x), self._root(y)
        if x == y:
            return
        if x > y:
            x, y = y, x
        self._table[x] += self._table[y]
        self._table[y] = x
    
    def same(self, x, y):
        return self._root(x) == self._root(y)

    def count_members(self, x):
        return -self._table[self._root(x)]
    
    def count_groups(self):
        return len({self._root(i) for i in range(n)})
    
    def __str__(self):
        return str([self._root(i) for i in range(n)])
    
    def __repr__(self):           
        return repr([self._root(i) for i in range(n)])

n, m, k, *ABCD = map(int, open(0).read().split())
AB = zip(ABCD[:2*m][::2], ABCD[:2*m][1::2])
CD = zip(ABCD[2*m:][::2], ABCD[2*m:][1::2])

uf = UnionFind(n)

friends = [set() for _ in range(n)]
for a, b in AB:
    a, b = a-1, b-1
    uf.unite(a, b)
    friends[a].add(b)
    friends[b].add(a)
    
blocks = [set() for _ in range(n)]
for c, d in CD:
    c, d = c-1, d-1
    if uf.same(c, d):
        blocks[c].add(d)
        blocks[d].add(c)

candidates = []
for i in range(n):
    candidates.append(uf.count_members(i)-len(friends[i])-len(blocks[i])-1)
print(*candidates)