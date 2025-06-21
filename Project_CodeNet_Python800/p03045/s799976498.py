N,M=map(int,input().split())
tree=[[]for i in range(N)]
ischecked=[0]*N
ans=0
for i in range(M):
    X,Y,Z=map(int,input().split())
    tree[X-1].append(Y-1)
    tree[Y-1].append(X-1)
for i in range(N):
    if ischecked[i]==1:
        continue
    ischecked[i]=1
    q=tree[i]
    while q:
        a=q.pop()
        if ischecked[a]==1:
            continue
        ischecked[a]=1
        q.extend(tree[a])
    ans=ans+1
print(ans)