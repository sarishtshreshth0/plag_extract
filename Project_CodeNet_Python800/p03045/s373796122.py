import sys
sys.setrecursionlimit(10**7)

def update(v):
    for nv in con[v]:
        if seen[nv]:
            continue
        seen[nv]=1
        update(nv)

N,M=map(int,input().split())
seen=[0]*N
con=[[] for i in range(N)]
cnt=[[i,0] for i in range(N)]
for i in range(M):
    X,Y,Z=map(int,input().split())
    X,Y=X-1,Y-1
    con[X].append(Y)
    con[Y].append(X)
    cnt[X][1]+=1
    cnt[Y][1]+=1
cnt.sort(key=lambda x:x[1],reverse=True)
ans=0
for i,a in cnt:
    if(seen[i]):
        continue
    ans+=1
    seen[i]=1
    update(i)
print(ans)