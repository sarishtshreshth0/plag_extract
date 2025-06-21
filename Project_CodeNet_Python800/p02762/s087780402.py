import sys
sys.setrecursionlimit(10**5)

def DFS(i,g):
    if i not in done:
        done.add(i)
        circle.add(i)
        g_list[i]=g
        for f in F[i]:
            DFS(f,g)
    else:
        return

N,M,K=map(int,input().split())
F=[[] for _ in range(N)]
B=[[] for _ in range(N)]

for f in range(M):
    f1,f2=map(int,input().split())
    F[f1-1].append(f2-1)
    F[f2-1].append(f1-1)
for b in range(K):
    b1,b2=map(int,input().split())
    B[b1-1].append(b2-1)
    B[b2-1].append(b1-1)

Group=[]
circle=set()
done=set()
g_list=[0 for _ in range(N)]
g=0
for i in range(N):
    if i not in done:
        DFS(i,g)
        Group.append(circle)
        circle=set()
        g+=1

ans=[-1 for _ in range(N)]
for i in range(N):
    G=g_list[i]
    ans[i]+=len(Group[G])
    for fr in F[i]:
        if fr in Group[G]:
            ans[i]-=1
    for bl in B[i]:
        if bl in Group[G]:
            ans[i]-=1

print(*ans)