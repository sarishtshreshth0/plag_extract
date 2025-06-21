n,m = map(int,input().split())
par = [i for i in range(n)]
rank = [0 for i in range(n)]

def find(x, par):
    if x == par[x]:
        return par[x]
    else:
        return find(par[x], par)
def unite(x, y, par, rank):
    x = find(x, par)
    y = find(y, par)
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

for i in range(m):
    x,y,z = map(int,input().split())
    unite(x-1, y-1, par, rank)
for i in range(n):
    par[i] = find(par[i], par)

T = list(set(par))
print(len(T))
