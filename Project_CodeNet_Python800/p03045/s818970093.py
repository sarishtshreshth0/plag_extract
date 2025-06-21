from collections import deque
N,M=map(int,input().split())
tree=[[] for _ in range(N)]
colornum=[-1]*N
for i in range(M):
    x,y,z=map(int,input().split())
    tree[x-1].append(y-1)
    tree[y - 1].append(x - 1)
#print(tree)
for i in range(N):
    d=deque()
    if colornum[i]==-1:
        d.append(i)
        colorid = i
    else:
        colorid=colornum[i]
    while len(d)>0:
        v=d.popleft()
        colornum[v]=colorid
        for j in tree[v]:
            if colornum[j]==-1:
                d.append(j)
print(len(set(colornum)))