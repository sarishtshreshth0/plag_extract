import sys
import itertools


class UnionFindTree:
    def __init__(self, n: int) -> None:
        self.par = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


def resolve(in_):
    N, M, K = map(int, in_.readline().split())
    ab = tuple(tuple(map(int, line.split())) for line in itertools.islice(in_, M))
    cd = tuple(tuple(map(int, line.split())) for line in itertools.islice(in_, K))

    ng = [set() for _ in range(N + 1)]
    friends_tree = UnionFindTree(N + 1)

    for a, b in ab:
        friends_tree.unite(a, b)
    for a, b in ab:
        if friends_tree.same(a, b):
            ng[a].add(b)
            ng[b].add(a)
    for c, d in cd:
        if friends_tree.same(c, d):
            ng[c].add(d)
            ng[d].add(c)
    ok = [0] * (N + 1)
    for i in range(1, N + 1):
        ok[friends_tree.find(i)] += 1    

    ans = [0] * (N + 1)
    for i in range(1, N + 1):
        ans[i] = ok[friends_tree.find(i)] - len(ng[i]) - 1

    return ' '.join(map(str, ans[1:]))


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
