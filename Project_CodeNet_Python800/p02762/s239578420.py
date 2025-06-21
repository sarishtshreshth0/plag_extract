n,m,k=map(int,input().split())
edge=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    edge[a].append(b)
    edge[b].append(a)

from collections import deque
label=[-1]*n

i=0
for start in range(n):
    if label[start]!=-1:
        continue
    else:
        i+=1
        label[start]=i    
    f=deque([start])
    while f:
        v=f.popleft()        
        for e in edge[v]:
            if label[e]==-1:
                label[e]=i
                f.append(e)   

Renketsu=[0]*(n+1)

for i in label:
    Renketsu[i]+=1

Block=[0]*n
for _ in range(k):
    c,d=map(int,input().split())
    c,d=c-1,d-1
    if label[c]==label[d]:
        Block[c]+=1
        Block[d]+=1

ans=[]
for k in range(n):
    ans.append(Renketsu[label[k]]-1 - len(edge[k]) - Block[k])
print(*ans)