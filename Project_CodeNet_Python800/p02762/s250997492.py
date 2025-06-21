import sys

ris=lambda:map(int,next(sys.stdin).split())

N,M,K=ris()

adj=[set() for _ in range(N)]
for _ in range(M):
    A,B=ris()
    A,B=A-1,B-1
    adj[A].add(B)
    adj[B].add(A)

colors=[-1]*N
ct={}
color=-1
for u in range(N):
    if colors[u]!=-1:
        continue
    color+=1
    colors[u]=color
    stk=[u]
    while stk:
        u=stk.pop()
        ct[color]=ct.get(color,0)+1
        for v in adj[u]:
            if colors[v]==-1:
                colors[v]=color
                stk.append(v)

blk=[{*()} for _ in range(N)]
for _ in range(K):
    A,B=ris()
    A,B=A-1,B-1
    if colors[A]==colors[B]:
        blk[A].add(B)
        blk[B].add(A)

ans=[0]*N
for u in range(N):
    c=colors[u]
    g=len(adj[u])
    b=len(blk[u])
    k=ct[c]-1-g-b
    ans[u]=k

print(*ans)
