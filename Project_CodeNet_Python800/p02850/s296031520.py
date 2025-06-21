from collections import deque

N=int(input())
G=[[] for _ in [0]*(N+1)]
for i in range(1,N):
    a,b=map(int,input().split())
    G[a].append((b,i))
    G[b].append((a,i))

root,res=0,0
for i in range(1,N+1):
    tmp=len(G[i])
    if tmp>res:
        res=tmp
        root=i
        
q=deque()
q.append((root,0))
color=[0]*N
D=[N+10]*(N+1)
D[root]=0
while q:
    p,c=q.popleft()
    nc=1
    while G[p]:
        np,ni=G[p].pop()
        if D[np]>D[p]:
            D[np]=D[p]+1
            if nc==c:
                nc+=1
            color[ni]=nc
            q.append((np,nc))
            nc+=1
print(res,*color[1:],sep='\n')