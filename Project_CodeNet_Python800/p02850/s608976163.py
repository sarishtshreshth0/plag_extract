from collections import deque

N=int(input())
E={i:set() for i in range(1,N+1)}
F=[0]*(N+1)

H=[0]*(N-1)
J={}
for s in range(N-1):
    a,b=map(int,input().split())
    E[a].add(b)
    E[b].add(a)
    F[a]+=1
    F[b]+=1
    H[s]=(a,b)
    J[(a,b)]=s

M=max(F)

C=[0]*(N-1)
G=[set() for _ in range(N+1)]
A=[-1]*(N+1)

T={i:False for i in range(1,N+1)}
T[1]=True
Q=deque([1])
while Q:
    v=Q.popleft()
    y=1
    for w in E[v]:
        if not T[w]:
            T[w]=True
            Q.append(w)
            
            p,q=min(v,w),max(v,w)

            c=(A[v]+y)%M
            
            A[w]=c
            C[J[(p,q)]]=c
            G[p].add(c)
            G[q].add(c)
            y+=1

print(max(C)+1)
print("\n".join(map(lambda x:str(x+1),C)))

