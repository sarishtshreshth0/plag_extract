class UnionFind:
    N = 0
    cost = 0
    par = []
    group = 0
    
    def init(N):
        UnionFind.N = N
        UnionFind.group = N
        UnionFind.par = [i for i in range(N)]

    def find(v):
        c = 0
        u = v
        while v != UnionFind.par[v]:
            v = UnionFind.par[v]
            c += 1

        if c > 10:
            while u != v: u, UnionFind.par[u] = UnionFind.par[u], v

        return v

    def union(v, u, c=0):
        vr = UnionFind.find(v)
        ur = UnionFind.find(u)

        if vr == ur: return True

        UnionFind.par[ur] = vr
        UnionFind.cost += c
        UnionFind.group -= 1
        
        return False
            
    def get_cost():
        return UnionFind.cost

    def get_group():
        return UnionFind.group

    def same(v, u):
        return UnionFind.find(v) == UnionFind.find(u)

N, M = list(map(int, input().split()))
UnionFind.init(N)

for i in range(M):
    x, y, _ = list(map(int, input().split()))
    x -= 1; y -= 1

    UnionFind.union(x, y)

print(UnionFind.get_group())