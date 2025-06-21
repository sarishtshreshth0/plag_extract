import sys
read = sys.stdin.read
def main():
    def find(x):
        if par[x] < 0:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        else:
            if par[x] > par[y]:
                x, y = y, x
            par[x] += par[y]
            par[y] = x
            return True
    def same(x, y):
        return find(x) == find(y)
    def size(x):
        return -par[find(x)]

    n, m, k = map(int, input().split())
    par = [-1] * n
    r = [-1] * n
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        unite(a, b)
        r[a] -= 1
        r[b] -= 1
    for i1 in range(n):
        r[i1] += size(i1)
    m = map(int, read().split())
    cd = zip(m, m)
    for c, d in cd:
        c -= 1
        d -= 1
        if same(c, d):
            r[c] -= 1
            r[d] -= 1
    print(*r, end=' ')

if __name__ == '__main__':
    main()