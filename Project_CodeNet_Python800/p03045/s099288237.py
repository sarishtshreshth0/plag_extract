N, M = map(int, input().split())
par = [i for i in range(N+1)]
h = [1 for _ in range(N+1)]

def root(x):
    if par[x] == x:
        return x
    par[x] = root(par[x])
    return par[x]

def unite(x,y):
    rx = root(x)
    ry = root(y)
    if h[rx] < h[ry]:
        rx, ry = ry, rx
    h[rx] += h[ry]
    par[ry] = rx

for _ in range(M):
    x,y,z = map(int, input().split())
    unite(x,y)

for i in range(1,N+1):
    par[i] = root(i)

print(len(set(par[1:])))
