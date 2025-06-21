N,M,K=map(int,input().split())

adj=[set() for _ in range(N)]
for _ in range(M):
    A,B=map(int,input().split())
    A,B=A-1,B-1
    adj[A].add(B)
    adj[B].add(A)

blk=[{*()} for _ in range(N)]
for _ in range(K):
    A,B=map(int,input().split())
    A,B=A-1,B-1
    blk[A].add(B)
    blk[B].add(A)

#print(adj)
#print(blk)

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


ans=[0]*N
for u in range(N):
    c=colors[u]
    k=ct[c]-1-len(adj[u])
    for v in blk[u]:
        if colors[v]==c:
            k-=1
    ans[u]=k

print(*ans)
