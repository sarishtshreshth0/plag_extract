import sys
sys.setrecursionlimit(10**7)

def update(v):
    for nv in G[v]:
        if seen[nv]:
            continue
        seen[nv]=1
        update(nv)

N,M=map(int,input().split())
seen=[0]*N
G=[[] for i in range(N)]
for i in range(M):
    X,Y,Z=map(int,input().split())
    X,Y=X-1,Y-1
    G[X].append(Y)
    G[Y].append(X)
ans=0
for i in range(N):
    if(seen[i]):
        continue
    ans+=1
    seen[i]=1
    update(i)
print(ans)