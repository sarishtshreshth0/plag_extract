N,M = map(int,input().split())

# parent(親)
par = [i for i in range(N+1)]
# rank(深さ)
rank = [0 for i in range(N+1)]
# 同グループの頂点数
size = [1 for i in range(N+1)]

# 木の根を求める
def root(x):
    if par[x] == x:             # 根の時
        return x
    else:
        par[x] = root(par[x])   # 経路圧縮
        return par[x]

# xとyの属する集合を併合(ランク有)
def unite(x,y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        par[x] = y              # xの親をyに
        size[y] += size[x]      # yの頂点数+=xの頂点数
    else:
        par[y] = x              # yの親をxに
        size[x] += size[y]      # xの頂点数+=yの頂点数
        if rank[x] == rank[y]:
            rank[x] += 1

for _ in range(M):
    x,y,z = map(int,input().split())
    unite(x,y)
ans = 0
for i in range(1,N+1):
    if par[i] == i:
        ans += 1
print(ans)