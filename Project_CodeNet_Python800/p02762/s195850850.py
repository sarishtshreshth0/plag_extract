from collections import Counter


class UnionFind:
    from collections import deque

    def __init__(self, v):
        self.v = v
        self._tree = list(range(v + 1))

    def _root(self, a):
        queue = self.deque()
        while self._tree[a] != a:
            queue.append(a)
            a = self._tree[a]
        while queue:
            index = queue.popleft()
            self._tree[index] = a
        return a

    def union(self, a, b):
        root_a = self._root(a)
        root_b = self._root(b)
        self._tree[root_b] = root_a

    def find(self, a, b):
        return self._root(a) == self._root(b)


N, M, K = map(int, input().split(' '))

n_friends = Counter()
n_groups = Counter()
uf = UnionFind(N)

for _ in range(M):
    a, b = map(int, input().split(' '))
    a -= 1
    b -= 1
    uf.union(a, b)
    n_friends[a] -= 1
    n_friends[b] -= 1

for _ in range(K):
    c, d = map(int, input().split(' '))
    c -= 1
    d -= 1
    if uf.find(c, d):
        n_friends[c] -= 1
        n_friends[d] -= 1

for n in range(N):
    n_groups[uf._root(n)] += 1

print(*[n_friends[n] + n_groups[uf._root(n)] - 1 for n in range(N)])
