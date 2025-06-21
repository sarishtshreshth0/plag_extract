import sys

rl=lambda:next(sys.stdin)
rfs=lambda:rl().split()
ris=lambda:map(int,rfs())

N,M,K=ris()

adj=[{*()} for _ in range(N)]
for _ in range(M):
    A,B=ris()
    A,B=A-1,B-1
    adj[A].add(B)
    adj[B].add(A)

c=-1
cs=[c]*N
ct={}
for u in range(N):
    if cs[u]!=-1:
        continue
    c+=1
    cs[u]=c
    stk=[u]
    while stk:
        u=stk.pop()
        if c not in ct:
            ct[c]=0
        ct[c]+=1
        for v in adj[u]:
            if cs[v]!=-1:
                continue
            cs[v]=c
            stk.append(v)

ans=[0]*N
for u in range(N):
    g=ct[cs[u]]-1
    f=len(adj[u])
    ans[u]=g-f

for _ in range(K):
    A,B=ris()
    A,B=A-1,B-1
    if cs[A]==cs[B]:
        ans[A]-=1
        ans[B]-=1

print(*ans)
