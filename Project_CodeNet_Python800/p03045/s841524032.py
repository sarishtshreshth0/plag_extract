def find(x):
    while G[x][0]!=x:
        x = G[x][0]
    return x
def union(x,y):
    xa = find(x)
    ya = find(y)
    if G[xa][1]>=G[ya][1]:
        G[ya][0] = xa
        G[xa][1] = max(G[xa][1],G[ya][1]+1)
    else:
        G[xa][0] = ya
        G[ya][1] = max(G[ya][1],G[xa][1]+1)
N,M = map(int,input().split())
G = {i:[i,0] for i in range(1,N+1)}
for _ in range(M):
    x,y,z = map(int,input().split())
    union(x,y)
hist = [0 for _ in range(N+1)]
for i in range(1,N+1):
    x = find(i)
    hist[x] = 1
print(sum(hist))